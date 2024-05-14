## Starting and Closing the Client Properly
**Remember** to call `start` and `close` or use the `async with` syntax!
```py
import enka

async with enka.GenshinClient() as client:
    ...

# Or
client = enka.GenshinClient()
await client.start()
...
await client.close()
```

## Finding Model's Attributes
If you're using an IDE like pycharm or VSCode, you can `alt + left click` on a variable and it will lead you the source code of the wrapper, from there you can see the model's docstring.
```py
class Artifact(BaseModel):
    """
    Represents an artifact.

    Attributes:
        id (int): The artifact's ID.
        main_stat_id (int): The main stat's ID.
        sub_stat_ids (List[int]): The sub stats' IDs.
        level (int): The artifact's level.
        equip_type (EquipmentType): The artifact's type (e.g. FLOWER, GOBLET, etc.).
        icon (str): The artifact's icon.
        item_type (ItemType): The artifact's type.
        name (str): The artifact's name.
        rarity (int): The artifact's rarity.
        main_stat (MainStat): The artifact's main stat.
        sub_stats (List[SubStat]): The artifact's sub stats.
        set_name (str): The artifact's set name.
    """
```

## Catching exceptions

All exception classes can be found in [enka/errors.py](https://github.com/seriaati/enka-py/blob/main/enka/errors.py), Catch them with `try-except`.
```py
import enka

async with enka.GenshinClient() as client:
    try:
        await client.fetch_showcase(901211014)
    except enka.errors.GameMaintenanceError:
        print("Game is in maintenance.")
```
