class BaseClass:
    def __init__(self,health,mana):
        self.health = health
        self.mana = mana
        self.current_health = self.health
        self.current_mana = self.mana

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
        if(self.current_health - damage < 0):
            self.current_health = 0

        self.current_health = self.current_health - damage



    def take_healing(self,healing):
        if(self.currentHealth == 0):
            return False    

        if(self.current_health + healing > self.health):
            self.current_health = self.health



