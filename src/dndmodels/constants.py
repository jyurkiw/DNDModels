from enum import StrEnum


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
