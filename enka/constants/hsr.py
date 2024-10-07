from __future__ import annotations

from typing import Literal

from ..enums.hsr import Element

__all__ = ("ASCENSION_TO_MAX_LEVEL", "DEFAULT_STATS", "DMG_BONUS_PROPS", "PERCENT_STAT_TYPES")

PERCENT_STAT_TYPES = {
    "CriticalChance",
    "CriticalDamage",
    "BreakDamageAddedRatio",
    "BreakDamageAddedRatioBase",
    "HealRatio",
    "SPRatio",
    "StatusProbability",
    "StatusResistance",
    "CriticalChanceBase",
    "CriticalDamageBase",
    "HealRatioBase",
    "SPRatioBase",
    "StatusProbabilityBase",
    "StatusResistanceBase",
    "PhysicalAddedRatio",
    "PhysicalResistance",
    "FireAddedRatio",
    "FireResistance",
    "IceAddedRatio",
    "IceResistance",
    "ThunderAddedRatio",
    "ThunderResistance",
    "WindAddedRatio",
    "WindResistance",
    "QuantumAddedRatio",
    "QuantumResistance",
    "ImaginaryAddedRatio",
    "ImaginaryResistance",
    "HPAddedRatio",
    "AttackAddedRatio",
    "DefenceAddedRatio",
    "HealTakenRatio",
}

ASCENSION_TO_MAX_LEVEL: dict[Literal[0, 1, 2, 3, 4, 5, 6], Literal[20, 30, 40, 50, 60, 70, 80]] = {
    0: 20,
    1: 30,
    2: 40,
    3: 50,
    4: 60,
    5: 70,
    6: 80,
}

DMG_BONUS_PROPS = {
    Element.PHYSICAL: "PhysicalAddedRatio",
    Element.FIRE: "FireAddedRatio",
    Element.LIGHTNING: "ThunderAddedRatio",
    Element.ICE: "IceAddedRatio",
    Element.QUANTUM: "QuantumAddedRatio",
    Element.WIND: "WindAddedRatio",
    Element.IMAGINARY: "ImaginaryAddedRatio",
}

DEFAULT_STATS: dict[str, float] = {
    "BaseHP": 0,
    "HPAddedRatio": 0,
    "HPDelta": 0,
    "HPConvert": 0,
    "BaseAttack": 0,
    "AttackAddedRatio": 0,
    "AttackDelta": 0,
    "AttackConvert": 0,
    "BaseDefence": 0,
    "DefenceAddedRatio": 0,
    "DefenceDelta": 0,
    "DefenceConvert": 0,
    "BaseSpeed": 0,
    "SpeedAddedRatio": 0,
    "SpeedDelta": 0,
    "SpeedConvert": 0,
    "CriticalChance": 0,
    "CriticalChanceBase": 0,
    "CriticalDamage": 0,
    "CriticalDamageBase": 0,
    "SPRatio": 0,
    "SPRatioBase": 0,
    "SPRatioConvert": 0,
    "StatusProbability": 0,
    "StatusProbabilityBase": 0,
    "StatusProbabilityConvert": 0,
    "StatusResistance": 0,
    "StatusResistanceBase": 0,
    "StatusResistanceConvert": 0,
    "HealRatioBase": 0,
    "HealRatioConvert": 0,
    "HealTakenRatio": 0,
    "ShieldAddedRatio": 0,
    "ShieldTakenRatio": 0,
    "AggroBase": 0,
    "AggroAddedRatio": 0,
    "AggroDelta": 0,
    "BreakDamageAddedRatio": 0,
    "BreakDamageAddedRatioBase": 0,
    "AllDamageTypeResistance": 0,
    "PhysicalResistanceDelta": 0,
    "FireResistanceDelta": 0,
    "IceResistanceDelta": 0,
    "ThunderResistanceDelta": 0,
    "QuantumResistanceDelta": 0,
    "ImaginaryResistanceDelta": 0,
    "WindResistanceDelta": 0,
    "PhysicalPenetrate": 0,
    "FirePenetrate": 0,
    "IcePenetrate": 0,
    "ThunderPenetrate": 0,
    "QuantumPenetrate": 0,
    "ImaginaryPenetrate": 0,
    "WindPenetrate": 0,
    "AllDamageTypeTakenRatio": 0,
    "PhysicalTakenRatio": 0,
    "FireTakenRatio": 0,
    "IceTakenRatio": 0,
    "ThunderTakenRatio": 0,
    "QuantumTakenRatio": 0,
    "ImaginaryTakenRatio": 0,
    "WindTakenRatio": 0,
    "AllDamageTypeAddedRatio": 0,
    "DOTDamageAddedRatio": 0,
    "PhysicalAddedRatio": 0,
    "FireAddedRatio": 0,
    "IceAddedRatio": 0,
    "ThunderAddedRatio": 0,
    "QuantumAddedRatio": 0,
    "ImaginaryAddedRatio": 0,
    "WindAddedRatio": 0,
    "StanceBreakAddedRatio": 0,
    "AllDamageReduce": 0,
    "FatigueRatio": 0,
    "MinimumFatigueRatio": 0,
}
