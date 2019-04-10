from Hero import Hero

class Dungeon:
    def __init__(self,file_name):
        self.file_name = file_name
        self.map = []
    def print_map(self):
        f = open(self.file_name,"r")
        matrix = []
        for line in f:
            lst = list(line)
            matrix.append(lst)
        self.map = matrix

    def spawn(self,hero):
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
        cordX = 0
        cordY = 0
        for index,lst in enumerate(self.map):

            for ind,el in enumerate(lst):
                if(el == "H"):
                    cordX = index
                    cordY = ind
                    break



        
d = Dungeon("level1.txt")
h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

d.print_map()
d.spawn(h)


d.spawn(h)

d.move_hero("right")