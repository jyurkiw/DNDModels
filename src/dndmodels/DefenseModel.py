from dataclasses import dataclass
from .constants import Resistance, DamageType


@dataclass(frozen=True)
class DefenseActor(object):
    armor_class: int = 10
    resistance: Resistance = Resistance.NORMAL
    resistance_type: DamageType = DamageType.FIRE
