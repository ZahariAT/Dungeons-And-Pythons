from BaseClass import BaseClass


class Enemy(BaseClass):
    def __init__(self,health, mana, damage):

        BaseClass.__init__(self,health,mana)
        self.damage = damage


en = Enemy(100,20,20)

print(en.is_alive())






