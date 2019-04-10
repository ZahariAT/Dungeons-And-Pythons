from BaseClass import BaseClass
from Weaponclass import Weapon
from Spell import Spell
class Hero(BaseClass):
    def __init__(self,name,title, health,mana,mana_regeneration_rate):
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        BaseClass.__init__(self,health,mana)
        self.weapon = None
        self.magic = None
    def known_as(self):
        return "{0} the {1}".format(self.name,self.title)

    

    def take_mana(self,mana_points):
        #to impelemnt increasing of mana when hero moves
        


        if(self.current_mana + mana_points > self.mana):
            self.current_mana = self.mana


        self.current_mana = self.current_mana + mana_points

    def equip(self,weapon):
        self.weapon = weapon

    def learn(self,spell):
        self.spell = spell

    def attack(self,s):
        if(s == "weapon"):
            if(self.weapon == None):
                return "The Hero doesn't have any weapon"
            else:
                return self.weapon.damage
        elif(s == "spell"):
            if(self.magic == None):
                return "The Hero doesn't "

            else:
                return self.magic.damage

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
s = Spell(name = "",damage =3000 , mana_cost =10 )
h.equip(w)
h.learn(s)
print(h.attack("weapon"))
