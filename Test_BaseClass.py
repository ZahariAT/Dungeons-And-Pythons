import unittest
from BaseClass import BaseClass
from Weaponclass import Weapon
class TestBaseClass(unittest.TestCase):
    def test_wrong_value_in_constructor(self):
        with self.assertRaises(ValueError):
            BaseClass(2,"Ivan")
        
    def test_attack_with_wrong_command(self):
        obj = BaseClass(3,4)
        weapon = Weapon("Despod",444)
        obj.equip(weapon)
        obj.attack("weapon")
        with self.assertRaises(ValueError):
            obj.attack("Genadi")






if __name__=='__main__':
    unittest.main()