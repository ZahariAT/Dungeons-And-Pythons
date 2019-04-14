import unittest
from Spell import Spell

class testSpell(unittest.TestCase):
    def test_when_incorect_type_name_is_given_in_constructor_Raise_ValueError(self):
        with self.assertRaises(ValueError):
            Spell(name=2, damage=2, mana_cost=2, cast_range=2)

    def test_if_a_spell_is_greater_than_other_Spell_by_damage_Return_True(self):
        self.assertEqual(True, Spell(name='who let', damage=30, mana_cost=30, cast_range=30) > Spell('the dogs out', 20, 20, 20))

    def test_when_spell_is_GT_than_not_spell_Raise_ValueError(self):
        with self.assertRaises(ValueError):
            Spell(name='who let', damage=30, mana_cost=30, cast_range=30) > 3

    def test__str__(self):
        self.assertEqual('Spell is Smooth criminal with damage: 1, cost: 1, range: 1', str(Spell('Smooth criminal', 1, 1, 1)))

if __name__=='__main__':
    unittest.main()