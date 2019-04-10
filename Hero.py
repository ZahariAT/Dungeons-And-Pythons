from BaseClass import BaseClass


class Hero(BaseClass):
    def __init__(self,name,title, health,mana,mana_regeneration_rate):
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        BaseClass.__init__(self,health,mana)


    def known_as(self):
        return "{0} the {1}".format(self.name,self.title)

    

    def take_mana(self,mana_points):
        #to impelemnt increasing of mana when hero moves
        


        if(self.current_mana + mana_points > self.mana):
            self.current_mana = self.mana


        self.current_mana = self.current_mana + mana_points





    def equip(self,weapon):
        pass

    def learn(self,spell):
        pass

    def attack(self,):
        pass




