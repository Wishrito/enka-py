from typing import Any, Dict, List

from pydantic import BaseModel, Field, model_validator

from .character import Character
from .player import Player

__all__ = ("GenshinShowcaseResponse",)


class GenshinShowcaseResponse(BaseModel):
    characters: List[Character] = Field(alias="avatarInfoList")
    player: Player = Field(alias="playerInfo")
    ttl: int
    uid: str

    @model_validator(mode="before")
    def _handle_no_showcase(cls, v: Dict[str, Any]) -> Dict[str, Any]:
        if "avatarInfoList" not in v or v["avatarInfoList"] is None:
            v["avatarInfoList"] = []
        return v
