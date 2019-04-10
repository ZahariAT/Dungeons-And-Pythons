from BaseClass import BaseClass


class Enemy(BaseClass):
    def __init__(self,health, mana, damage):

        BaseClass.__init__(self,health,mana)
        self.damage = damage
        





