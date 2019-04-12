from Hero import Hero
from Enemy import Enemy
from Weaponclass import Weapon
from Spell import Spell

class Fight:
    @staticmethod
    def fight_simulator(hero, enemy, attack_range, direction):
        if type(hero) != Hero or type(enemy) != Enemy:
            raise ValueError("Those types can't fight!")
        while hero.is_alive() and enemy.is_alive():
            if hero.can_cast():
                if hero.can_cast():
                    hero.attack('spell')
                    enemy.take_damage(hero.spell.damage)
                else:
                    hero.spell = None
                print('Hero attacked by spell!')

            elif hero.weapon != None:
                hero.attack('weapon')
                enemy.take_damage(hero.weapon.damage)
                print('Hero attacked!')
            else:
                print('Hero is not equipt.')
            if enemy.is_alive():
                if hero.spell != None:
                    print(attack_range)
                    if attack_range >= 1:  
                        attack_range -= 1
                        print('Enemy moved one step to the {}'.format(direction))
                    else:
                        if enemy.can_cast():
                            enemy.attack('spell')
                            hero.take_damage(enemy.spell.damage)
                        elif enemy.weapon != None:
                            enemy.attack('weapon')
                            hero.take_damage(enemy.weapon.damage)
                        else:
                            hero.take_damage(enemy.damage)
                        print('Enemy attacked!')
                else:
                    if enemy.can_cast():
                        enemy.attack('spell')
                        hero.take_damage(enemy.spell.damage)
                    elif enemy.weapon != None:
                        enemy.attack('weapon')
                        hero.take_damage(enemy.weapon.damage)
                    else:
                        hero.take_damage(enemy.damage)
                    print('Enemy attacked!')
            else:
                print('Enemy is dead')