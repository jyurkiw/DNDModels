from .AttackModel import DamageEvent as _DamageEvent
from .AttackModel import AttackActor as _AttackActor
from .DefenseModel import DefenseActor as _DefenseActor
from .constants import SaveTarget as _SaveTarget
from .constants import Situation as _Situation
from .constants import DamageType as _DamageType
from .constants import Resistance as _Resistance
from .constants import AttackerSimulationClassification as _AttackerSimulationClassification
from .constants import AttackerConstants as _AttackerConstants
from .constants import DefenderConstants as _DefenderConstants

DamageEvent = _DamageEvent
AttackActor = _AttackActor
DefenseActor = _DefenseActor

SaveTarget = _SaveTarget
Situation = _Situation
DamageType = _DamageType
Resistance = _Resistance
AttackerSimulationClassification = _AttackerSimulationClassification

AttackerConstants = _AttackerConstants
DefenderConstants = _DefenderConstants

def get_proficiency_bonus_string(bonus: int, has_proficiency: bool = True) -> str:
    """
    Calculates the proficiency bonus string based on the bonus value and whether proficiency is active.

    :param bonus: The numerical bonus value.
    :param has_proficiency: Whether the character has proficiency. Defaults to True. Typically only False when calculating
    saving throws.
    :return: A string representing the proficiency bonus (e.g., "+3", "-2", "+0").
    """
    if has_proficiency and bonus >= 0: return f"+{bonus}"
    elif bonus < 0: return f"-{abs(bonus)}"
    else: return "+0"

def get_situation_base_str(situation: Situation) -> str:
    """
    Returns the base dice notation string based on the current situation.

    :param situation: The current Situation enum value.
    :return: A string representing the base dice roll (e.g., "1d20", "1d20kh").
    """
    if situation == Situation.NORMAL:
        return "1d20"
    elif situation == Situation.ADVANTAGE:
        return "1d20kh"
    else:
        return "1d20kl"

def get_bonus_value(value: int) -> str:
    return f"+{value}" if value >= 0 else f"-{abs(value)}"
