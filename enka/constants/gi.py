from __future__ import annotations

from typing import Literal

__all__ = (
    "ASCENSION_TO_MAX_LEVEL",
    "CHARACTER_RARITY_MAP",
    "DMG_BONUS_FIGHT_PROPS",
    "PERCENT_STAT_TYPES",
)

PERCENT_STAT_TYPES = {
    "FIGHT_PROP_HP_PERCENT",
    "FIGHT_PROP_ATTACK_PERCENT",
    "FIGHT_PROP_DEFENSE_PERCENT",
    "FIGHT_PROP_CRITICAL",
    "FIGHT_PROP_CRITICAL_HURT",
    "FIGHT_PROP_CHARGE_EFFICIENCY",
    "FIGHT_PROP_HEAL_ADD",
    "FIGHT_PROP_PHYSICAL_ADD_HURT",
    "FIGHT_PROP_FIRE_ADD_HURT",
    "FIGHT_PROP_ELEC_ADD_HURT",
    "FIGHT_PROP_WATER_ADD_HURT",
    "FIGHT_PROP_WIND_ADD_HURT",
    "FIGHT_PROP_ROCK_ADD_HURT",
    "FIGHT_PROP_ICE_ADD_HURT",
    "FIGHT_PROP_GRASS_ADD_HURT",
}

CHARACTER_RARITY_MAP: dict[str, Literal[4, 5]] = {
    "QUALITY_ORANGE": 5,
    "QUALITY_ORANGE_SP": 5,
    "QUALITY_PURPLE": 4,
}

ASCENSION_TO_MAX_LEVEL: dict[Literal[0, 1, 2, 3, 4, 5, 6], Literal[20, 40, 50, 60, 70, 80, 90]] = {
    0: 20,
    1: 40,
    2: 50,
    3: 60,
    4: 70,
    5: 80,
    6: 90,
}

DMG_BONUS_FIGHT_PROPS = {
    "FIGHT_PROP_PHYSICAL_ADD_HURT",
    "FIGHT_PROP_FIRE_ADD_HURT",
    "FIGHT_PROP_ELEC_ADD_HURT",
    "FIGHT_PROP_WATER_ADD_HURT",
    "FIGHT_PROP_WIND_ADD_HURT",
    "FIGHT_PROP_ROCK_ADD_HURT",
    "FIGHT_PROP_ICE_ADD_HURT",
    "FIGHT_PROP_GRASS_ADD_HURT",
}
