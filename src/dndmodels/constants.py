from enum import StrEnum


class BaseStat(StrEnum):
    STRENGTH = "strength"
    DEXTERITY = "dexterity"
    CONSTITUTION = "constitution"
    INTELLIGENCE = "intelligence"
    WISDOM = "wisdom"
    CHARISMA = "charisma"

class AttackEvent(StrEnum):
    EVENT_TYPE = "event_type"
    NUM_TARGETS = "num_targets"
    DAMAGE_CODE = "damage_code"
    DAMAGE_TYPE = "damage_type"
    HIT_BONUS = "hit_bonus"
    SAVE_DC = "save_dc"
    SAVE_TYPE = "save_type"

class SaveEffect(StrEnum):
    HALF_DAMAGE = "half_damage"
    NEGATE_FULL = "negate_full"
    NEGATE_PARTIAL = "negate_partial"

class Situation(StrEnum):
    NORMAL = "Normal"
    ADVANTAGE = "Advantage"
    DISADVANTAGE = "Disadvantage"


class DamageType(StrEnum):
    SLASHING = "Slashing"
    BLUDGEONING = "Bludgeoning"
    PIERCING = "Piercing"
    ACID = "Acid"
    COLD = "Cold"
    FIRE = "Fire"
    LIGHTNING = "Lightning"
    THUNDER = "Thunder"
    POISON = "Poison"
    FORCE = "Force"
    PSYCHIC = "Psychic"
    RADIANT = "Radiant"
    NECROTIC = "Necrotic"


class Resistance(StrEnum):
    NORMAL = "Normal"
    RESISTANCE = "Resistance"
    IMMUNITY = "Immunity"
    VULNERABILITY = "Vulnerability"

class AttackerConstants(StrEnum):
    ATTACKERS = "attackers"
    PROFICIENCY = "proficiency"
    STAT_BONUS = "stat_bonus"
    ENCHANTMENT = "enchantment"
    SITUATION = "situation"

class DefenderConstants(StrEnum):
    DEFENDER = "defender"
    ARMOR_CLASS = "armor_class"
    RESISTANCE = "resistance"
    RESISTANCE_TYPE = "resistance_type"