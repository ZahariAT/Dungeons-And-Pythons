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
        name = input('Write a name for your hero: ')
        title = input('How is your hero known as: ')
        h = Hero(name=name, title=title, health=100, mana=100, mana_regeneration_rate=2)
        name = input('Give a name to your weapon: ')
        w = Weapon(name=name, damage=20)
        h.equip(w)
        print('\n{} will fight with {} to save The Princess!\n'.format(h.known_as(), w.name))
        input('Press enter to start the game!')
        map = Dungeon("level1.txt")
        map.spawn(h)
        map.print_map()
        input_data = input("Type w/s/a/d to move your hero up/down/left/right\
, f for fight, spawn for spawn, status to show hero's status or e for exit: ")
        while(input_data != 'e'):
            if input_data in command_list[0].keys():
                map.move_hero(command_list[0][input_data])
                map.print_map()
            elif input_data == command_list[1]:
                map.hero_attack()
                map.print_map()
            elif input_data == command_list[2]:
                map.spawn(h)
                map.print_map()
            elif input_data == command_list[3]:
                print('\n',h, h.weapon, h.spell)
            else:
                print('Not correct command!')
            print('\n')
            input_data = input("Type w/s/a/d to move your hero up/down/left/right\
, f for fight, spawn for spawn, status to show hero's status or e for exit: ")

if __name__ == '__main__':
    TheGame.lets_play()