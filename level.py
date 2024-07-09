
class Level:
    def __init__(self, hero, objects):
        self.hero = hero
        self.objects = objects

    def getHero(self):
        return self.hero

    def getObjects(self):
        return self.objects