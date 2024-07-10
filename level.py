from object import Object 

class Level:
    def __init__(self, hero, objects):
        self.hero = hero
        self.objects = objects

    def getHero(self):
        return self.hero

    def getObjects(self):
        return self.objects
    
def levelBuilder():
    objects = []

    file_name = "fase1.txt"
    
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line_index, line in enumerate(lines):
        for character_index, caractere in enumerate(line):
            if caractere == '0':
                objects.append(Object(character_index*32, line_index*32, 'assets/wall_0.png', solid=True))
            elif caractere == 'H':
                hero = Object(character_index*32, line_index*32, 'assets/hero_0.png', solid=False)
            elif caractere == 'T':
                objects.append(Object(character_index*32, line_index*32, 'assets/tree_0.png', solid=True))
            elif caractere == 'C':
                objects.append(Object(character_index*32, line_index*32, 'assets/coin_0.png', solid=False))
            elif caractere == 'M':
                objects.append(Object(character_index*32, line_index*32, 'assets/monster_0.png', solid=True))

    level1 = Level(hero, objects)
    return level1