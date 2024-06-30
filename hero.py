import pygame
import os;

RUNNING = [pygame.image.load(os.path.join("assets/hero", "hero_0.png")),
           pygame.image.load(os.path.join("assets/hero", "hero_1.png")),
           pygame.image.load(os.path.join("assets/hero", "hero_2.png")),
           pygame.image.load(os.path.join("assets/hero", "hero_3.png"))]

SPEED = 0.2

class Hero():
    def __init__(self):
        self.step_index = 0
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.color = (255, 255, 255)
        self.speed_x = 0
        self.speed_y = 0
        self.x = 300
        self.y = 300

    # Eventos
    def trate_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.speed_y = -SPEED
            elif event.key == pygame.K_s:
                self.speed_y = SPEED
            elif event.key == pygame.K_a:
                self.speed_x = -SPEED
            elif event.key == pygame.K_d:
                self.speed_x= SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.speed_y = 0
            elif event.key == pygame.K_s:
                self.speed_y = 0
            elif event.key == pygame.K_a:
                self.speed_x = 0
            elif event.key == pygame.K_d:
                self.speed_x = 0

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