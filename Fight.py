from Hero import Hero
from Enemy import Enemy
from Weaponclass import Weapon
from Spell import Spell

class Fight:
    @staticmethod
    def fight_simulator(hero, enemy, attack_range, direction):
        if type(hero) != Hero or type(enemy) != Enemy:
            raise ValueError("Those types can't fight!")
        print('A fight is started between our {} and {}!'.format(hero, enemy))
       
        def has_spell_or_weapon(attacker, defender, attack_range):
            if attacker.can_cast():
                attacker.attack('spell')
                defender.take_damage(attacker.spell.damage)
                print('{t} casts a {s}! {t} hits {t2} for {d} dmg. {t2} health is {h}'.format(t = type(attacker).__name__,
                    t2 = type(defender).__name__, s = attacker.spell.name, d = attacker.spell.damage, h = defender.current_health))
                return True
            elif attacker.weapon != None:
                if attack_range > 0:
                    print('Hero we wait for enemy to come!')
                    return True
                attacker.attack('weapon')
                defender.take_damage(attacker.weapon.damage)
                print('{t} attacked with {w}! {t} hits {t2} for {d} dmg. {t2} health is {h}'.format(t = type(attacker).__name__,
                    t2 = type(defender).__name__, w = attacker.weapon.name, d = attacker.weapon.damage, h = defender.current_health))
                return True
            return False

        while hero.is_alive() and enemy.is_alive():
            if not has_spell_or_weapon(hero, enemy, attack_range):
                print('Hero is not well equipt.')
            if enemy.is_alive():
                if not enemy.can_cast():
                    if attack_range >= 1 :  
                        attack_range -= 1
                        print('Enemy moved one step to the {}.'.format(direction))
                    else:
                        if not has_spell_or_weapon(enemy, hero, attack_range):
                            hero.take_damage(enemy.damage)
                            print('Enemy attacked!')
                elif enemy.can_cast():
                    if enemy.spell.cast_range >= attack_range:
                        enemy.attack('spell')
                        hero.take_damage(enemy.spell.damage)
                        print('Enemy casts a {}!'.format(enemy.spell.name ))
                else:
                    if not has_spell_or_weapon(enemy, hero, attack_range):
                        hero.take_damage(enemy.damage)
                        print('Enemy attacked!')
            else:
                print('Enemy is dead')
                return True
        print('Hero is dead :( ')
        return False