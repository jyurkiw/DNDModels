from dataclasses import dataclass
from .constants import Resistance, DamageType, DefenderConstants


@dataclass(frozen=True)
class DefenseActor(object):
    armor_class: int = 10
    resistance: Resistance = Resistance.NORMAL
    resistance_type: DamageType = DamageType.FIRE

    @staticmethod
    def from_json(json_data):
        return DefenseActor(**json_data)
