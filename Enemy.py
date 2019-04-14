from BaseClass import BaseClass
import type_checker

class Enemy(BaseClass):
    @type_checker.type_checker(int, int, int)
    def __init__(self,health, mana, damage):

        BaseClass.__init__(self,health,mana)
        self.damage = damage
        self.cord_x = None
        self.cord_Y = None

    def __str__(self):
        return 'Enemy(health={}, mana={}, damage={})'.format(self.current_health, self.current_mana, self.damage)






