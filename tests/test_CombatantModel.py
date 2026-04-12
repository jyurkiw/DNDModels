import unittest
from parameterized import parameterized
from src.dndmodels.CombatantModel import CombatantModel, CombatException
from src.dndmodels.constants import BaseStat

class TestCombatantModel(unittest.TestCase):
    def setUp(self):
        self.test_combatant = CombatantModel(
            name = "test combatant",
            strength_bonus=1,
            dexterity_bonus=2,
            constitution_bonus=3,
            intelligence_bonus=4,
            wisdom_bonus=5,
            charisma_bonus=6
        )

    @parameterized.expand([
        (BaseStat.STRENGTH, 1),
        (BaseStat.DEXTERITY, 2),
        (BaseStat.CONSTITUTION, 3),
        (BaseStat.INTELLIGENCE, 4),
        (BaseStat.WISDOM, 5),
        (BaseStat.CHARISMA, 6)
    ])
    def test_combatant_model_get_stat_bonus__stats_exist(self, stat, expected_value):
        expected = expected_value
        actual = self.test_combatant.get_stat_bonus(stat=stat)
        self.assertEqual(expected, actual)

    def test_combatant_model_get_stat_bonus__stat_does_not_exist(self):
        stat = "comeliness"
        with self.assertRaises(CombatException) as ce:
            self.test_combatant.get_stat_bonus(stat=stat)


if __name__ == '__main__':
    unittest.main()
