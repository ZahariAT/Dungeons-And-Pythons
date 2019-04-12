class Weapon:
    def __init__(self, name, damage):
        if type(name) != str or type(damage) != int:
            raise ValueError('Not correct type!')
        self.weapen_name = name
        self.damage = damage
    def __str__(self):
        return str((self.name,self.damage))