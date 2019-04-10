class Hero:
    def __init__(self,name,title, health,mana,mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.currenthealt = self.health
        self.currentMana = self.mana   

    def known_as(self):
        return "{0} the {1}".format(self.name,self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if(self.health > 0):
            return True

        return False

    def can_cast(self):
        if(self.mana > 0):
            return True

        return False

    def take_damage(self,damage):
        self.health = self.health - damage




    def take_healing(self,healing)
        if(self.currentHealth == 0):
            return False    

        if(self.health + healing) 