class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        if type(name) != str or type(damage) != int or type(mana_cost) != int:
            raise ValueError('Not correct type!') 
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range


    def __str__(self):
        return str((self.name,self.damage,self.mana_cost,self.cast_range))