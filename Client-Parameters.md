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

## Cache
*Added in v2.3.0*  
  
Caching is not enabled by default, passing in any subclass of `enka.cache.BaseTTLCache` will enable caching.  
See [`example/cache.py`](https://github.com/seriaati/enka-py/blob/main/examples/cache.py) on how to enable memory caching and sqlite caching.
```py
import enka

async with enka.GenshinClient(cache=enka.cache.SQLiteCache()) as client:
   ...

# Same goes for HSRClient
```
You can add your own implementation of caching (e.g. Redis) by subclassing `enka.cache.BaseTTLCache` and implementing all the abstract methods.