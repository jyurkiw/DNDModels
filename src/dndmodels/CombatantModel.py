from dataclasses import dataclass
from abc import ABC, abstractmethod

from src.dndmodels import DamageType
from src.dndmodels.constants import BaseStats


class CombatException(Exception):
    pass

@dataclass(frozen=True)
class AbstractAttackEvent(ABC):
    num_targets: int
    damage_code: str
    damage_type: DamageType


@dataclass(frozen=True)
class HitAttackEvent(AbstractAttackEvent):
    hit_bonus: int


@dataclass(frozen=True)
class SaveAttackEvent(AbstractAttackEvent):
    save_dc: int
    save_type: str


@dataclass(frozen=True)
class AbstractCombatantModel(ABC):
    name: str

    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    proficiency_bonus: str
    initiative: int

    hit_points: int
    armor_class: str

    attacks: list[AbstractAttackEvent]

    def get_stat_bonus(self, stat: str) -> int:
        if stat not in BaseStats._value2member_map_:
            raise CombatException(f"{stat} is not a valid stat. Failure trying to get_stat_bonus for {self.name}")
        return getattr(self, stat)


@dataclass(frozen=True)
class CombatantModel(AbstractCombatantModel):
    pass
