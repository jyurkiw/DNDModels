from dataclasses import dataclass, field
from typing import Optional
from .DefenseModel import DefenseActor
from .constants import DamageType, Situation, AttackerSimulationClassification, SaveTarget
from roller import Roll
from . import get_proficiency_bonus_string, get_situation_base_str, get_bonus_value


class SimulationException(Exception):
    pass

@dataclass(frozen=True)
class _BaseAttackActor(object):
    actor_name: str = ""
    proficiency: int = 2
    save_dc: int = 0
    situation: Situation = Situation.NORMAL


# SINGLE TARGET MODELS
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

# ROLLER TARGET MODELS
@dataclass(frozen=True)
class RollerDamageResult(object):
    value: int
    type: DamageType = DamageType.FIRE


@dataclass(frozen=True)
class RollerDamageEvent(object):
    source_name: str
    damage_code: str
    damage_results: list[RollerDamageResult] = field(default_factory=list)


@dataclass(frozen=True)
class RollerAttackAction(object):
    """
    is_save_based: If True, the hit roll is based on a failed defender saving throw instead of an attacker hit roll.

    save_target: SaveTarget value

    damage_code: XdY+Z

    num_uses: Number of times the attack can be used per sim. If the attack has a recharge_value, leave num_uses defaulted.
    priority: Priority of attack in random attack selection (see weighting in Random.choices method).
    is_aoe: True if the attack is an AoE. Attack is repeated num_targets times. is_save_based must be True.
    num_targets: If attack is_aoe, damage is applied num_targets times with a save for each based on the defender save value.

    has_recharge: Attack will be preferred even if attacker strategy is random as long as num_uses is > 0. num_uses
    cannot be greater than 1. If num_uses is 0, recharge will be tested at the start of the turn and num_uses will be set
    equal to 1.
    recharge_values: If the result of a roller.roll using recharge_code is found in recharge_values, set num_uses equal to 1.
    recharge_code: Roll to determine recharge. Is almost always 1d6, recharge on 6 (both are defaults).

    is_multiattack: True if this attack is part of a multiattack sequence. Additional attacks in the multiattack sequence
    should be set as riders to one main attack and will be executed in depth-first-search order. Multiattacks should
    generally have a very high priority value.

    riders: Riders are damage effects that trigger off of other attacks succeeding. Unless is_multiattack is True, a
    rider's attack roll or saving throw will be skipped. An example of a typical rider is the poison damage on an
    assassin's dagger that occurs automatically without a saving throw if the dagger attack hits.
    requires_advantage: Rider only occurs if the attacker situation is set to ADVANTAGE.
    """
    attack_name:str = ""

    is_save_based: bool = False

    stat_bonus: int = 0
    enchantment: int = 0

    save_target: SaveTarget = SaveTarget.DEXTERITY

    damage_code: str = "1d6"

    num_uses: int = 1
    priority: int = 1
    is_aoe: bool = False
    num_targets: int = 3

    has_recharge: bool = False
    recharge_values: set[int] = field(default_factory=set)
    recharge_code: str = "1d6"

    is_multiattack: bool = False

    riders: list[Optional["RollerAttackAction"]] = field(default_factory=list)
    requires_advantage: bool = False

    @property
    def can_use(self):
        return self.num_uses > 0

    @staticmethod
    def from_json(parsed_json):
        pass

    def decrement_uses(self):
        object.__setattr__(self, "num_uses", self.num_uses - 1)

    def roll_to_hit(self, attacker: _BaseAttackActor, target: DefenseActor) -> tuple[bool, Roll]:
        hit_code = ''.join([
            get_situation_base_str(attacker.situation),
            get_proficiency_bonus_string(attacker.proficiency),
            get_bonus_value(self.stat_bonus),
            get_bonus_value(self.enchantment)
        ])
        attack_roll = Roll(hit_code)
        return attack_roll.total >= target.armor_class, attack_roll

    def roll_save(self, attacker: _BaseAttackActor, target: DefenseActor) -> tuple[bool, Roll]:
        save_code = ''.join([

        ])



@dataclass(frozen=True)
class RollerAttackActor(_BaseAttackActor):
    attacker_sim_class: AttackerSimulationClassification = AttackerSimulationClassification.NORMAL
    attack_actions: list[RollerAttackAction] = field(default_factory=list)

    @staticmethod
    def from_json(parsed_json) -> _BaseAttackActor:
        return RollerAttackActor(
            actor_name=parsed_json["name"],
            proficiency=parsed_json["proficiency"],
            attack_actions=[RollerAttackAction.from_json(attack_action) for attack_action in parsed_json["attack_actions"]],
            situation=Situation(parsed_json["situation"])
        )

    def select_attack(self) -> RollerAttackAction:
        """Handle attack selection logic and return the correct attack action."""
        pass

    def make_attack(self, attack_action: RollerAttackAction, target: DefenseActor, ) -> list[tuple[str, Roll]]:
        """Execute the attack logic. Either hit roll or saving throw depending on attack action state.

        :param attack_action: The attack to make.
        :param target: The target to attack.
        :return: All rolls made to resolve the attack.
        """
        if attack_action.is_aoe and not attack_action.is_save_based:
            raise SimulationException(f"is_save_based must be True if is_aoe is True: [attack_name]: {attack_action.attack_name}")
        if self.attacker_sim_class == AttackerSimulationClassification.NORMAL:
            if not attack_action.is_save_based:
                return self.make_basic_attack(attack_action, target)
            else:
                return self.make_basic_save(attack_action, target)
        else:
            raise NotImplementedError(f"Attacker class {self.attacker_sim_class} not implemented")

    def make_basic_attack(self, attack_action: RollerAttackAction, target: DefenseActor) -> tuple(bool, list[tuple[str, Roll]]):
        """Make an attack against the target's AC

        :returns tuple [success bool, list[tuple[source str, attack Roll]]]
        """



    def make_basic_save(self, attack_action: RollerAttackAction, target: DefenseActor) -> list[tuple[str, Roll]]:
        """Make a saving throw against the attacker's spell save DC."""
        pass