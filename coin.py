import pygame
import os;
import random

IMGS = [pygame.image.load(os.path.join("assets/coin", "coin_0.png"))]

class Coin():
    def __init__(self):
        self.color = (255, 50, 50)
        self.image = IMGS[0]
        self.rect = self.image.get_rect()
        self.x = random.randint(1,800)
        self.y = random.randint(1,600)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))