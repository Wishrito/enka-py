# About `BaseClient`
Both `GenshinClient` and `HSRClient` are subclasses of the `BaseClient`, it has the following parameters:

## Language
Changes the language of contents returned by the wrapper, such as weapon names, character names, etc.
```py
import enka

# With enum
async with enka.GenshinClient(enka.gi.Language.RUSSIAN) as client:
    ...

async with enka.HSRClient(enka.hsr.Language.THAI) as client:
    ...

# Or with str
async with enka.GenshinClient("ru") as client:
    ...

async with enka.HSRClient("th") as client:
    ...

```

## Headers
Changes the headers when requesting to the Enka Network API, default is `{"User-Agent": "enka-py"}`
```py
import enka

async with enka.GenshinClient(headers={"User-Agent": "MyDiscordBot-1.0"}) as client:
    ...

# Same goes for HSRClient
```

## Cache TTL
The time to live (ttl) in seconds for the internal cache to be evicted, the default is 60 seconds, which is the minimum refresh time in Enka Network. Increasing this value might result in inconsistency between the data returned by the wrapper and the live data.
```py
import enka

async with enka.GenshinClient(cache_ttl=30) as client:
   ...

# Same goes for HSRClient
```