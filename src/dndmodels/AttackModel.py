from dataclasses import dataclass
from .constants import DamageType, Situation, AttackerConstants


@dataclass(frozen=True)
class DamageEvent(object):
    source_name: str
    number: int = 1
    sides: int = 6
    bonus: int = 0
    type: DamageType = DamageType.SLASHING

    def get_damage_code(self):
        damage_code = f"{self.number}d{self.sides}"
        if self.bonus != 0:
            damage_code += f" {'+' if self.bonus > 0 else '-'} {self.bonus}"
        return damage_code

    @staticmethod
    def from_json(json_dict):
        return DamageEvent(**json_dict)


@dataclass(frozen=True)
class AttackActor(object):
    attacker_name: str = ""
    proficiency: int = 2
    stat_bonus: int = 0
    enchantment: int = 0
    situation: Situation = Situation.NORMAL

    @staticmethod
    def from_json(parsed_json):
        return AttackActor(**parsed_json)
