import type_checker

class Spell:
    #@type_checker.type_checker(str, int, int, int)
    def __init__(self, name, damage, mana_cost, cast_range):
        if type(name) != str or type(damage) != int or type(mana_cost) != int:
            raise ValueError('Not correct type!') 
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __gt__(self, other):
        if type(other) is not Spell:
            raise ValueError('Can not compare those types!')
        return self.damage > other.damage