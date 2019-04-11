from Hero import Hero
from Weaponclass import Weapon
from Spell import Spell
from random import *



class Dungeon:
    def __init__(self,file_name):
        self.file_name = file_name
        self.map = []
        self.lst_treasures = []
        self.hero = None

    def create_treasure(self):
        count = 0
        for lst in self.map:
            for el in lst:
                if(el == "T"):
                    count +=1
        for num in range(count):
            rand_number = randint(1,4)
            if(rand_number == 1):
                pass
    def print_map(self):
        f = open(self.file_name,"r")
        matrix = []
        for line in f:
            lst = list(line)
            matrix.append(lst)

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

        for lst in self.map:
            for el in lst:
                print(el,end = "")
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
            pass
        elif(self.map[new_cordY][new_cordX] == "G"):
            pass
        elif(self.map[new_cordY][new_cordX] == "E"):
            pass


        self.hero.mana += self.hero.mana_regeneration_rate

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
h.equip(w)
s = Spell(name="Fireball", damage=30, mana_cost=50)
h.learn(s)
map = Dungeon("level1.txt")
map.spawn(h)
map.print_map()
map.move_hero("right")
map.move_hero("down")
