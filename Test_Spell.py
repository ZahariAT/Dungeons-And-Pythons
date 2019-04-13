import unittest
from Spell import Spell

class testSpell(unittest.TestCase):
    def test_when_incorect_type_name_is_given_in_constructor_Raise_ValueError(self):
        with self.assertRaises(ValueError):
            Spell(2, 2, 2, 2)

    def test_if_a_spell_is_greater_than_other_Spell_by_damage_Return_True(self):
        self.assertEqual(True, Spell('who let', 30, 30, 30) > Spell('the dogs out', 20, 20, 20))

    def test_when_spell_is_GT_than_not_spell_Raise_ValueError(self):
        with self.assertRaises(ValueError):
            Spell('who let', 30, 30, 30) > 3

if __name__=='__main__':
    unittest.main()