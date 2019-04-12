from Hero import Hero
from Weaponclass import Weapon
from Spell import Spell
from random import *
from Fight import Fight
from Enemy import Enemy


all_treasures = ["Mana potion","Health potion",("Expecto Patronum",40,50,3),("The Axe of Destiny",30),
"Mana potion","Health potion",("Accio",20,30,2),("Holy Carver",20),
"Mana potion","Health potion",("Wingardium Leviosa",30,40,1),("Blade of a Thousand Cuts",40)]


enemies = [(130,40,50),(150,20,30),(111,100,40),(170,120,40),(160,80,30,Spell("lol",30,50,1))]




class Dungeon:
    def __init__(self,file_name):
        self.map = []
        with open(file_name) as f:
            for line in f.readlines():
                self.map.append(list(line))
        self.lst_treasures = []
        self.hero = None


    def print_map(self):
        if(len(self.map) == 0):
            self.map = matrix
        

        for lst in self.map:
            for el in lst:
                print(el,end = "")          
    def spawn(self,hero):
        if(self.hero == None):

            self.hero = hero
        check_is_there_starting_point = False
        for index,lst in enumerate(self.map):
            for ind,el in enumerate(lst):
                if(el == "S"):
                    check_is_there_starting_point = True
                    self.map[index][ind] = "H"

        if(not check_is_there_starting_point):
            print ("There not any more spawning points")
            return 
    def hero_attack(self):
        pass
    def move_hero(self,direction):
        old_cordX = 0
        old_cordY = 0 
        for index,lst in enumerate(self.map):

            for ind,el in enumerate(lst):
                if(el == "H"):
                    old_cordY = index
                    old_cordX = ind
                    break
        print(old_cordY,old_cordX)
        new_cordX = old_cordX
        new_cordY = old_cordY
        if(direction == "right"):
            new_cordX = old_cordX + 1
            if(new_cordX > len(self.map[0])):
                print("The hero is outside the matrix")
                return False
        elif(direction == "left"):
            new_cordX = old_cordX - 1
            if(new_cordX < 0):
                print("The hero is outside the matrix")
                return False
        elif(direction == "up"):
            new_cordY = old_cordY -1
            if(new_cordY < 0):
                print("The hero is outside the matrix")
                return False
        elif(direction == "down"):
            new_cordY = old_cordY + 1
            if(new_cordY > len(self.map) - 1):
            
                print("The hero is outside the matrix")
                return False
        else:
            print("Command not appropriate")
            return False

        print(new_cordY,new_cordX)
        if(self.map[new_cordY][new_cordX] == "."):
            self.map[new_cordY][new_cordX] = "H"
            self.map[old_cordY][old_cordX] = "."
        elif(self.map[new_cordY][new_cordX] == "#"):
            print("There is obstacle")
            return
        elif(self.map[new_cordY][new_cordX] == "T"):
            rand_number = randint(0,len(all_treasures) - 1)
            print(rand_number)
            if(not len(all_treasures[rand_number]) == 2 or not len(all_treasures[rand_number]) == 4):
                if("Health" in all_treasures[rand_number]):
                    self.hero.current_health = self.hero.health
                    print("The hero's health is full")
                else:
                    self.hero.current_mana = self.hero.mana
                    print("The hero's mana is full")
            elif(len(all_treasures[rand_number] == 2)):
                weap = Weapon(all_treasures[rand_number][0],all_treasures[rand_number][1])
                self.hero.weapon = weap

                print("hero has new weapon")
            elif(len(all_treasures[rand_number] == 4)):
                sp = Spell(all_treasures[rand_number][0],all_treasures[rand_number][1],all_treasures[rand_number][2],all_treasures[rand_number][3])
                self.hero.spell = sp
                print("hero has new spell")
            else:
                print("Not correct")
                return

            self.map[new_cordY][new_cordX] = "H"
            self.map[old_cordY][old_cordX] = "."
            self.coord_X = new_cordX
            self.coord_Y = new_cordY
        elif(self.map[new_cordY][new_cordX] == "G"):
            print("The hero have reached the final of this level!")
            return
        elif(self.map[new_cordY][new_cordX] == "E"):
            pass

        if(self.hero.current_mana < self.hero.mana):

            self.hero.current_mana += self.hero.mana_regeneration_rate

    def hero_attack(self, by=None):
        for y, order in enumerate(self.map):
            for x in range(len(order)):
                if self.map[y][x] == 'H':
                    break
            if self.map[y][x] == "H":
                break
        def can_attack(cast_range):
            i = 0
            while i <= cast_range:
                if self.map[y][x + i] == 'E':
                    Fight().fight_simulator(self.hero, Enemy(100, 100, 20), i, 'left')
                    return True
                elif self.map[y + i][x] == 'E':
                    Fight().fight_simulator(self.hero, Enemy(100, 100, 20), i, 'up')
                    return True
                elif self.map[y][x - i] == 'E':
                    Fight().fight_simulator(self.hero, Enemy(100, 100, 20), i, 'right')
                    return True
                elif self.map[y - i][x] == 'E':
                    Fight().fight_simulator(self.hero, Enemy(100, 100, 20), i, 'down')
                    return True
                i += 1
            print('No enemy within range')
            return False
        cast_range = 0
        if self.hero.spell != None:
            cast_range = self.hero.spell.cast_range
        can_attack(cast_range)

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
h.equip(w)
s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
h.learn(s)
map = Dungeon("level1.txt")
map.spawn(h)
map.print_map()
map.move_hero("right")
map.move_hero("down")
map.print_map()
map.hero_attack(by="spell")
map.move_hero("down")
map.move_hero("down")
map.print_map()
map.hero_attack(by="spell")
print(h)
map.move_hero("right")
print(h)
map.print_map()
