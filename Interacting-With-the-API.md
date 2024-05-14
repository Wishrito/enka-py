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

## Namecards and icons
*Available after v1.2.0*  
  
Character icons are now `Icon` objects, you can access all types of icons from it:
- `icon.side`: https://enka.network/ui/UI_AvatarIcon_Side_Ambor.png
- `icon.circle`: https://enka.network/ui/UI_AvatarIcon_Ambor_Circle.png
- `icon.gacha`:  https://enka.network/ui/UI_Gacha_AvatarImg_Ambor.png
- `icon.front`: https://enka.network/ui/UI_AvatarIcon_Ambor.png

The same goes for `ShowcaseCharacter.costume_icon` and `Player.profile_picture_icon`.

Namecards are now `Namecard` objects:
- `Namecard.icon`: https://enka.network/ui/UI_NameCardIcon_0.png
- `Namecard.full`: https://enka.network/ui/UI_NameCardPic_0_P.png

## Stats
*Available after v1.4.0*  
  
Stats refer to character, weapon, and artifact stats.  
Internally, stats for characters are `FightProp` classes, while the others are `Stat` classes; they can be accessed in the same way, but their `type`s are different (`FightPropType` and `StatType`).  
For your convenience, there are `stat.is_percentage` and `stat.formatted_value` to use, for exmple:  
- If `stat.type` is `StatType.FIGHT_PROP_CUR_ATTACK`
  - `stat.is_percentage = False`
  - `stat.formatted_value = '2300'`
- If `stat.type` is `StatType.FIGHT_PROP_CRITICAL`
  - `stat.is_percentage = True`
  - `stat.formatted_value = '23.1%'`

## Constellations
*Available after v1.7.0*  
  
After v1.7.0, all constellations that belong to a character will appear in `Character.constellations`, the `Constellation.unlocked` attribute will indicate whether the constellation is unlocked. Also, there is a new attribute `Character.constellations_unlocked` that indicates how many constellations the character has unlocked.

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
You can find more detailed examples in the [/examples](https://github.com/seriaati/enka-py/tree/main/examples) folder.