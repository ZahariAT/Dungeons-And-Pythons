from Weaponclass import Weapon
from Spell import Spell
from Enemy import Enemy
from Hero import Hero
from Dungeon import Dungeon
import type_checker
from pprint import pprint


class TheGame:
    @staticmethod
    def lets_play():
        command_list = [{'w':'up', 's':'down', 'a':'left', 'd':'right'}, 'f', 'spawn', 'status']
        print('\nLets play a game!\n ')
        w = Weapon(name="The Axe of Destiny", damage=20)
        name = input('Write a name for your hero: ')
        title = input('How is your hero known as: ')
        h = Hero(name=name, title=title, health=100, mana=100, mana_regeneration_rate=2)
        h.equip(w)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=4)
        h.learn(s)
        print('\n',h.known_as(), 'will fight to save The Princess!\n')
        map = Dungeon("level1.txt")
        map.spawn(h)
        map.print_map()
        input_data = input("Type w/s/a/d to move your hero up/down/left/right\
, f for fight, spawn for spawn, status to show hero's status or e for exit: ")
        while(input_data != 'e'):
            if input_data in command_list[0].keys():
                map.move_hero(command_list[0][input_data])
            elif input_data == command_list[1]:
                map.hero_attack()
            elif input_data == command_list[2]:
                map.spawn(h)
            elif input_data == command_list[3]:
                print('\n',h, h.weapon, h.spell)
            else:
                print('Not correct command!')
            print('\n')
            map.print_map()
            input_data = input("Type w/s/a/d to move your hero up/down/left/right\
, f for fight, spawn for spawn, status to show hero's status or e for exit: ")

if __name__ == '__main__':
    TheGame.lets_play()