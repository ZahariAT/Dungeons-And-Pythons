from Hero import Hero
from Enemy import Enemy
from Weaponclass import Weapon
from Spell import Spell

class Fight:
    @staticmethod
    def fight_simulator(hero, enemy):
        if type(hero) != Hero or type(enemy) != Enemy:
            raise ValueError("Those types can't fight!")
        while hero.is_alive() and enemy.is_alive():
            if hero.magic != None:
                if hero.can_cast():
                    hero.attack('spell')
                    enemy.take_damage(hero.magic.spell_damage)
                else:
                    hero.magic = None
            elif hero.weapon != None:
                hero.attack('weapon')
                enemy.take_damage(hero.weapon.damage)
            else:
                print('Hero is not equipt.')
            if enemy.is_alive():
                if enemy.magic != None:
                    if enemy.can_cast():
                        enemy.attack('spell')
                        hero.take_damage(enemy.magic.spell_damage)
                    else:
                        enemy.magic = None
                elif enemy.weapon != None:
                    enemy.attack('weapon')
                    hero.take_damage(enemy.weapon.damage)
                else:
                    enemy.damage
                    hero.take_damage(enemy.damage)
Fight().fight_simulator(1,2)