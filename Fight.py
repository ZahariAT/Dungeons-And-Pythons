from Hero import Hero
from Enemy import Enemy
from Weaponclass import Weapon
from Spell import Spell

class Fight:
    @staticmethod
    def fight_simulator(hero, enemy, attack_range, direction):
        if type(hero) != Hero or type(enemy) != Enemy:
            raise ValueError("Those types can't fight!")
        def spell_or_weapon(attacker, defender):
            if attacker.can_cast():
                attacker.attack('spell')
                defender.take_damage(attacker.spell.damage)
                print('{} attacked with {}!'.format(type(attacker).__name__, attacker.spell.name))
                return True
            elif attacker.weapon != None:
                attacker.attack('weapon')
                defender.take_damage(attacker.weapon.damage)
                print('{} attacked with {}!'.format(type(attacker).__name__, attacker.weapon.name))
                return True
            return False

        while hero.is_alive() and enemy.is_alive():
            if not spell_or_weapon(hero, enemy):
                print('Hero is not equipt.')
            if enemy.is_alive():
                if hero.can_cast() and not enemy.can_cast():
                    if attack_range >= 1:  
                        attack_range -= 1
                        print('Enemy moved one step to the {}'.format(direction))
                    else:
                        if not spell_or_weapon(enemy, hero):
                            hero.take_damage(enemy.damage)
                            print('Enemy attacked!')
                else:
                    if not spell_or_weapon(enemy, hero):
                        hero.take_damage(enemy.damage)
                        print('Enemy attacked!')
            else:
                print('Enemy is dead')
                return True
        print('Hero is dead :( ')
        return False