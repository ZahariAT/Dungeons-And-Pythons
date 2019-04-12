class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        if type(name) != str or type(damage) != int or type(mana_cost) != int:
            raise ValueError('Not correct type!') 
        self.spell_name = name
        self.spell_damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
