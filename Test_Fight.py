import unittest
from Fight import Fight
from Hero import Hero
from Enemy import Enemy
from Weaponclass import Weapon
from Spell import Spell

class testFight(unittest.TestCase):
    def test_when_Hero_wins(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.equip(w)
        self.assertEqual(True, Fight().fight_simulator(h, Enemy(10, 10, 10), 0, 'up'))

    def test_when_Hero_Loose(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(False, Fight().fight_simulator(h, Enemy(1, 10, 100), 0, 'up'))


if __name__=='__main__':
    unittest.main()