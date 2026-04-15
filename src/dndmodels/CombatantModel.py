from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json

from .constants import BaseStat, SaveEffect, DamageType


class CombatException(Exception):
    pass


@dataclass_json
@dataclass(frozen=True)
class AbstractAttackEvent(object):
    name: str = ""
    damage_code: str = "1d6"
    damage_type: DamageType = DamageType.SLASHING
    misc_damage_bonus: int = 0


@dataclass_json
@dataclass(frozen=True)
class HitAttackEvent(AbstractAttackEvent):
    crit_damage_code: str = "1d6"
    crit_numbers: set[int] = field(default_factory=lambda: {20})
    bonus_stat: BaseStat = BaseStat.STRENGTH
    enchantment_bonus: int = 0


@dataclass_json
@dataclass(frozen=True)
class SaveAttackEvent(AbstractAttackEvent):
    save_dc: int = 10
    save_stat: BaseStat = BaseStat.DEXTERITY
    save_effect: SaveEffect = SaveEffect.NEGATE_FULL


@dataclass_json
@dataclass(frozen=True)
class AbstractCombatantModel(object):
    name: str = ""

    strength_bonus: int = 0
    dexterity_bonus: int = 0
    constitution_bonus: int = 0
    intelligence_bonus: int = 0
    wisdom_bonus: int = 0
    charisma_bonus: int = 0

    proficiency_bonus: int = 2
    #initiative_bonus: int = 2

    #hit_points: int = 0
    armor_class: int = 10

    attacks: Optional[list[HitAttackEvent|SaveAttackEvent]] = None

    def get_stat_bonus(self, stat: str) -> int:
        if stat not in BaseStat._value2member_map_:
            raise CombatException(f"{stat} is not a valid stat. Failure trying to get_stat_bonus for {self.name}")
        return getattr(self, stat)


@dataclass_json
@dataclass(frozen=True)
class CombatantModel(AbstractCombatantModel):
    pass
