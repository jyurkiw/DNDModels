from enum import StrEnum


class SaveTarget(StrEnum):
    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"

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

class AttackerSimulationClassification(StrEnum):
    """Attacker Classifications
    Normal: Attacks are executed once in the order they appear in the attacks list.
    Limited: Limited uses, then disabled. If used alone first attack is used until no uses remain, then next attack is used.
    Random: Attack is selected every round using random.choices with RollerAttackAction.priority passed as weight.
    Limited_Random: Randomly select attacks from the attacks list weighted by priority. Exclude attack if RollerAttackAction.num_uses = 0
    """
    NORMAL = "Normal"
    LIMITED = "Limited"
    RANDOM = "Random"
    LIMITED_RANDOM = "Limited Random"


class Resistance(StrEnum):
    NORMAL = "Normal"
    RESISTANCE = "Resistance"
    IMMUNITY = "Immunity"
    VULNERABILITY = "Vulnerability"

class AttackerConstants(StrEnum):
    ATTACKER = "attacker"
    PROFICIENCY = "proficiency"
    STAT_BONUS = "stat_bonus"
    ENCHANTMENT = "enchantment"
    SITUATION = "situation"

class DefenderConstants(StrEnum):
    DEFENDER = "defender"
    ARMOR_CLASS = "armor_class"
    RESISTANCE = "resistance"
    RESISTANCE_TYPE = "resistance_type"