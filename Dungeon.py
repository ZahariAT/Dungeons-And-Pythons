from Hero import Hero
from Weaponclass import Weapon
from Spell import Spell
from random import *
from Fight import Fight
from Enemy import Enemy


all_treasures = ["Mana potion","Health potion","Mana potion","Health potion","Mana potion","Health potion",("Expecto Patronum",40,50,3),("The Axe of Destiny",30),
("Accio",20,30,2),("Holy Carver",20),("Wingardium Leviosa",30,40,1),("Blade of a Thousand Cuts",40)]


enemies = [(130,40,20),(110,20,30),(111,100,40),(170,120,10),(160,80,30)]


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
        to_break = False
        for index,lst in enumerate(self.map):
            for ind,el in enumerate(lst):
                if(el == "S"):
                    check_is_there_starting_point = True
                    self.map[index][ind] = "H"
                    to_break = True
            

            if(to_break):
                break



        if(not check_is_there_starting_point):
            print ("There not any more spawning points")
            return 



  
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


        if(not self.hero.is_alive()):
            print("Game over")
            return
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

        if(self.map[old_cordY][old_cordX] == "S"):
            pass
        if(self.map[new_cordY][new_cordX] == "."):
            self.map[new_cordY][new_cordX] = "H"
            self.map[old_cordY][old_cordX] = "."
        elif(self.map[new_cordY][new_cordX] == "#"):
            print("There is obstacle")
            return
        elif(self.map[new_cordY][new_cordX == "S"]):
            #to finish
            self.map[new_cordX][new_cordX] = "H"
        elif(self.map[new_cordY][new_cordX] == "T"):
            rand_number = randint(0,len(all_treasures) - 1)
            print(rand_number)
            if(not len(all_treasures[rand_number]) == 2 and not len(all_treasures[rand_number]) == 4):
                if("Health" in all_treasures[rand_number]):
                    self.hero.current_health = self.hero.health
                    print("The hero's health is full")
                else:
                    self.hero.current_mana = self.hero.mana
                    print("The hero's mana is full")
            elif(len(all_treasures[rand_number]) == 2):
                weap = Weapon(all_treasures[rand_number][0],all_treasures[rand_number][1])
                self.hero.weapon = weap

                print("hero has new weapon")
            elif(len(all_treasures[rand_number]) == 4):
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
            self.hero_attack()
            if(self.hero.is_alive()):
                self.map[new_cordY][new_cordX] = "H"
                self.map[old_cordY][old_cordX] = "."
                
            else:
                print("Game Over. Hero died")
            

        if(self.hero.current_mana < self.hero.mana):

            self.hero.current_mana += self.hero.mana_regeneration_rate



    def hero_attack(self, by=None):
        if not self.hero.is_alive():
            print('Game over!')
            return
        for y, order in enumerate(self.map):
            for x in range(len(order)):
                if self.map[y][x] == 'H':
                    break
            if self.map[y][x] == "H":
                break
        tuple_enemy = enemies[randint(0, len(enemies) - 1)]
        if randint(0, 10) < 8:
            random_enemy = Enemy(tuple_enemy[0], tuple_enemy[1], tuple_enemy[2])
        else:
            tuple_spell = all_treasures[randint(6, len(all_treasures) - 1)]
            if len(tuple_spell)  == 4:
                random_enemy = Enemy(tuple_enemy[0], tuple_enemy[1], tuple_enemy[2])
                random_enemy.learn(Spell(tuple_spell[0], tuple_spell[1], tuple_spell[2], tuple_spell[3]))
            elif len(tuple_spell)  == 2:
                random_enemy = Enemy(tuple_enemy[0], tuple_enemy[1], tuple_enemy[2])
                random_enemy.equip(Weapon(tuple_spell[0], tuple_spell[1]))
            else:
                raise ValueError('Hero_attackError')

        def while_cast_range(cast_range, expr_y, expr_x, direction):
            _x, _y = x, y
            i = 0
            while i <= cast_range:
                temp_y = eval(expr_y)
                temp_x = eval(expr_x)
                if temp_x >= 0 and temp_x < len(self.map[0]) and temp_y >= 0 and temp_y < len(self.map):
                    if self.map[temp_y][temp_x] == '#':
                        return False
                    if self.map[temp_y][temp_x] == 'E':
                        if Fight().fight_simulator(self.hero, random_enemy, i, direction):
                            return (temp_y, temp_x)
                else:
                    return False
                i += 1
            #i -= 1
            return False

        def can_attack(cast_range):
            can_attack_right = while_cast_range(cast_range, 'y', 'x+i', 'left')
            if can_attack_right:
                return can_attack_right
            can_attack_left = while_cast_range(cast_range, 'y', 'x-i', 'right')
            if can_attack_left:
                return can_attack_left
            can_attack_up = while_cast_range(cast_range, 'y-i', 'x', 'down')
            if can_attack_up:
                return can_attack_up
            can_attack_down = while_cast_range(cast_range, 'y+i', 'x', 'up')
            if can_attack_down:
                return can_attack_down
            if self.hero.is_alive():
                print('No enemy within range!')
            return False

        cast_range = 0
        if self.hero.spell != None:
            cast_range = self.hero.spell.cast_range
        is_dot =  can_attack(cast_range)
        if is_dot:
            self.map[is_dot[0]][is_dot[1]] = '.'

        else:
            print("Game over")
            return
h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
h.equip(w)
s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=4)
h.learn(s)
map = Dungeon("level2.txt")
map.spawn(h)
map.print_map()
map.move_hero("right")
map.print_map()
map.move_hero("down")
map.print_map()
map.move_hero("down")
map.print_map()
map.move_hero("down")
map.print_map()
map.move_hero("right")
map.print_map()
map.move_hero("right")
map.print_map()
map.move_hero("right")
map.print_map()
map.move_hero("right")
map.print_map()
