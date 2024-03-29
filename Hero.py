from BaseClass import BaseClass
from Weaponclass import Weapon
from Spell import Spell
import type_checker
from random import *

quotes = ['The way get started is to quit talking and begin doing.', 'The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.', 'Don’t let yesterday take up too much of today.', 'You learn more from failure than from success. Don’t let it stop you. Failure builds character.', 'Failure will never overtake me if my determination to succeed is strong enough.']

class Hero(BaseClass):
    @type_checker.type_checker(str, str, int, int, int)
    def __init__(self,name,title, health,mana,mana_regeneration_rate):
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.money = 0
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
    
    @type_checker.type_checker(str)
    def update(self, which):
        if which == 'weapon':
            if self.weapon != None:
                if self.money >= self.weapon.update_cost: # money > weapon.update_cost
                    self.money -= self.weapon.update_cost
                    self.weapon.damage += 10
                    self.weapon.update_cost += 20
                    print('Update successful!')
                else:
                    print('Not enough money!')
            else:
                print("You don't have this equipment")
        elif which == 'spell':
            if self.spell != None:
                if self.money >= self.spell.update_cost: # money > spell.update_cost
                    self.money -= self.spell.update_cost
                    self.spell.update_cost += 20
                    self.spell.damage += 10
                    print('Update successful!')
                else:
                    print('Not enough money!')
            else:
                print("You don't have this equipment")
        elif which == 'spell/weapon':
            print('\nOh, you think out of the box! Well congratulations you found this message thanks to:')
            print('Whatislove and Zahari. Sponsored by HackBulgaria!')
            print('Here is a quote for you: {}'.format(quotes[randint(0, len(quotes) - 1)]))
        else:
            print("You don't have this equipment")

    def __str__(self):
        return 'Hero(health={}, mana={})'.format(self.current_health, self.current_mana)