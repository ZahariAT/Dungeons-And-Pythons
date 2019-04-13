class Weapon:
    def __init__(self, name, damage):
        if type(name) != str or type(damage) != int:
            raise ValueError('Not correct type!')
        self.ssname = name
        self.damage = damage

    def __gt__(self, other):
        if type(other) is not Weapon:
            raise ValueError('Can not compare those types!')
        return self.damage > other.damage