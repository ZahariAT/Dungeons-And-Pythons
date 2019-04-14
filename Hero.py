from BaseClass import BaseClass
from Weaponclass import Weapon
from Spell import Spell
import type_checker

class Hero(BaseClass):
    @type_checker.type_checker(str, str, int, int, int)
    def __init__(self,name,title, health,mana,mana_regeneration_rate):
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        BaseClass.__init__(self,health,mana)
        
    def known_as(self):
        return "{0} the {1}".format(self.name,self.title)

    @type_checker.type_checker(int)
    def take_mana(self,mana_points):
        #to impelemnt increasing of mana when hero moves
        

        if(self.current_mana + mana_points > self.mana):
            self.current_mana = self.mana


        else:
            self.current_mana = self.current_mana + mana_points



    def __str__(self):
        return 'Hero(health={}, mana={})'.format(self.current_health, self.current_mana)