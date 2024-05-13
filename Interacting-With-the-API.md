# Genshin Impact
To interact with the Enka Network Genshin Impact API, use the `GenshinClient`.  
```py
import enka

async with enka.GenshinClient() as client:
    await client.fetch_showcase(901211014)
```
Alternatively, call the `start` and `close` methods manually.
```py
import enka

client = enka.GenshinClient()
await client.start()
await client.fetch_showcase(901211014)
await client.stop()
```
> [!IMPORTANT]  
> When using the client, you **must** use either the `async with` syntax or call `start` and `stop` manually; otherwise, the client won't work and `RuntimeError` will be raised.

# Honkai: Star Rail
Similarly, to interact with the Enka Network HSR API, use the `HSRClient`.
```py
import enka

async with enka.HSRClient() as client:
    await client.fetch_showcase(809162009)
```
Same as `GenshinClient`, you can also call the `start` and `close` methods manually.
```py
import enka

client = enka.HSRClient()
await client.start()
await client.fetch_showcase(809162009)
await client.stop()
```

# Examples
You can find more detailed examples in the `/examples` folder.