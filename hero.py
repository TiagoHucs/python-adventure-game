import pygame
import os;

RUNNING = [pygame.image.load(os.path.join("assets/hero", "hero_0.png")),
           pygame.image.load(os.path.join("assets/hero", "hero_1.png")),
           pygame.image.load(os.path.join("assets/hero", "hero_2.png")),
           pygame.image.load(os.path.join("assets/hero", "hero_3.png"))]

class Hero():
    def __init__(self):
        self.step_index = 0
        self.image = RUNNING[0]
        self.color = (255, 255, 255)
        self.speed_x = 0
        self.speed_y = 0
        self.x = 300
        self.y = 300

    def update(self):
        self.y += self.speed_y
        self.x += self.speed_x
        self.step_index += 1
        if (self.step_index // 120) > 3:
            self.step_index = 0
        self.image = RUNNING[self.step_index // 120]
        if self.speed_x > 0:
            self.image = pygame.transform.flip(self.image, True, False)



    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))