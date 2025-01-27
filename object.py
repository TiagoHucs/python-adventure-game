import pygame

class Object:
    def __init__(self, x, y, image_path, solid=True):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.solid = solid

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y