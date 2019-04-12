class BaseClass:
    def __init__(self,health,mana):
        self.health = health
        self.mana = mana
        self.current_health = self.health
        self.current_mana = self.mana
        self.weapon = None
        self.spell = None
   

    def attack(self,s):
        if(s == "weapon"):
            if(self.weapon == None):
                return "The Hero doesn't have any weapon"
            else:
                return self.weapon.damage
        elif(s == "spell"):
            if(self.spell== None):
                return "The Hero doesn't "

            else:
                return self.magic.damage

    def equip(self,weapon):
        self.weapon = weapon

    def learn(self,spell):
        self.spell = spell


    def get_health(self):
        return self.current_health

    def get_mana(self):
        return self.current_mana

    def is_alive(self):
        if(self.current_health > 0):
            return True
        return False

    def can_cast(self):
        if(self.mana > 0):
            return True

        return False

    def take_damage(self,damage):
        if(self.current_health - damage < 0):
            self.current_health = 0
        else:
            self.current_health = self.current_health - damage



    def take_healing(self,healing):
        if(self.current_health == 0):
            print("Hero is dead")
            return False    
        if(self.current_health + healing > self.health):
            self.current_health = self.health


