import unittest
from Weaponclass import Weapon

class testWeapon(unittest.TestCase):
    def test_when_incorect_type_name_is_given_in_constructor_Raise_ValueError(self):
        with self.assertRaises(ValueError):
            Weapon(name=2, damage=2)

    def test_if_a_weapon_is_greater_than_other_weapon_by_damage_Return_True(self):
        self.assertEqual(True, Weapon(name='who let', damage=30) > Weapon(name='the dogs out', damage=20))

    def test_when_weapon_is_GT_than_not_weapon_Raise_ValueError(self):
        with self.assertRaises(ValueError):
            Weapon(name='who let', damage=30) > 3

if __name__=='__main__':
    unittest.main()