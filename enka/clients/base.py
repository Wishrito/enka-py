from __future__ import annotations

from typing import TYPE_CHECKING, Any

import aiohttp
import orjson
from loguru import logger

from ..errors import raise_for_retcode

if TYPE_CHECKING:
    from ..enums.enum import Game
    from .cache import BaseTTLCache


class BaseClient:
    """Base client with requesting capabilities."""

    def __init__(
        self,
        game: Game,
        *,
        headers: dict[str, Any] | None = None,
        cache: BaseTTLCache | None = None,
    ) -> None:
        self.game = game

        self._headers = headers or {"User-Agent": "enka-py"}
        self._session: aiohttp.ClientSession | None = None
        self._cache = cache

    async def __aenter__(self) -> BaseClient:
        await self.start()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self.close()

    async def start(self) -> None:
        """Start the client."""
        self._session = aiohttp.ClientSession(headers=self._headers)

    async def close(self) -> None:
        """Close the client."""
        if self._session is None:
            msg = f"Client is not started, call `{self.__class__.__name__}.start` first"
            raise RuntimeError(msg)

        await self._session.close()

    async def _request(self, url: str) -> dict[str, Any]:
        if self._session is None:
            msg = f"Client is not started, call `{self.__class__.__name__}.start` first"
            raise RuntimeError(msg)

        if self._cache is not None:
            await self._cache.clear_expired()
            cached = await self._cache.get(url)
            if cached is not None:
                return orjson.loads(cached.encode())

        logger.debug(f"Requesting {url}")

        async with self._session.get(url) as resp:
            if resp.status != 200:
                raise_for_retcode(resp.status)

            data: dict[str, Any] = await resp.json()
            if self._cache is not None:
                await self._cache.set(url, orjson.dumps(data).decode(), ttl=60)
            return data
