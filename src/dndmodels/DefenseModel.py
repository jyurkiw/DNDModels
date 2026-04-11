from dataclasses import dataclass, field
from .constants import Resistance, DamageType, SaveTarget, Situation
from . import get_proficiency_bonus_string, get_situation_base_str
from roller import Roll


@dataclass(frozen=True)
class DefenseActor(object):
    """Defense actor model.
    Attack actor model compatability:
        AttackActor
        _BaseAttackActor
        RollerAttackActor
    """
    armor_class: int = 10
    proficiency: int = 2

    save_situation: Situation = Situation.NORMAL
    save_proficiencies: set[SaveTarget] = field(default_factory=set)
    save_magic_bonus: int = 0
    save_expertise: set[SaveTarget] = field(default_factory=set)
    save_bonuses: dict[SaveTarget, int] = field(default_factory=dict)

    resistance: Resistance = Resistance.NORMAL
    resistance_type: DamageType = DamageType.FIRE

    @staticmethod
    def from_json(json_data):
        return DefenseActor(**json_data)

    def get_save_roll(self, save_stat: SaveTarget) -> Roll:
        return Roll("".join([
            get_situation_base_str(self.save_situation),
            get_proficiency_bonus_string(self.save_bonuses[save_stat], save_stat in self.save_proficiencies),
            get_proficiency_bonus_string(self.save_bonuses[save_stat], save_stat in self.save_expertise),
            f'+{self.save_magic_bonus}'
        ]))

    def roll_save(self, save_stat: SaveTarget, save_dc: int) -> tuple[bool, Roll]:
        saving_throw = self.get_save_roll(save_stat)
        return saving_throw.total >= save_dc, saving_throw
