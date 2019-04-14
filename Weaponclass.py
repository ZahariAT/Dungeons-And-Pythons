import type_checker

class Weapon:
    @type_checker.type_checker(str, int)
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __gt__(self, other):
        if type(other) is not Weapon:
            raise ValueError('Can not compare those types!')
        return self.damage > other.damage