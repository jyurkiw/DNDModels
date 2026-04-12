from enum import StrEnum


class BaseStat(StrEnum):
    STRENGTH = "strength_bonus"
    DEXTERITY = "dexterity_bonus"
    CONSTITUTION = "constitution_bonus"
    INTELLIGENCE = "intelligence_bonus"
    WISDOM = "wisdom_bonus"
    CHARISMA = "charisma_bonus"


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