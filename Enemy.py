from BaseClass import BaseClass


class Enemy(BaseClass):
    def __init__(self,health, mana, damage):

        BaseClass.__init__(self,health,mana)
        self.damage = damage
        self.cord_x = None
        self.cord_Y = None






