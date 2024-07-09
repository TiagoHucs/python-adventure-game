import pygame
import sys
from object import Object 
from functions import levelBuilder

# Inicialize o pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Legend of Dude")

# Definir a cor
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FLOOR = (0, 100, 0)

# Função principal
def main():
    clock = pygame.time.Clock()

    level = levelBuilder()
    personagem = level.getHero()
    objects = level.getObjects()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Movimentar o personagem com as setas do teclado
        movimento_x = 0
        movimento_y = 0

        if keys[pygame.K_LEFT]:
            movimento_x = -5
        if keys[pygame.K_RIGHT]:
            movimento_x = 5
        if keys[pygame.K_UP]:
            movimento_y = -5
        if keys[pygame.K_DOWN]:
            movimento_y = 5

        # Mover personagem e verificar colisão com objetos sólidos
        personagem.rect.x += movimento_x
        for obj in objects:
            if obj.solido and personagem.rect.colliderect(obj.rect):
                if movimento_x > 0:  # Movendo para a direita
                    personagem.rect.right = obj.rect.left
                if movimento_x < 0:  # Movendo para a esquerda
                    personagem.rect.left = obj.rect.right

        personagem.rect.y += movimento_y
        for obj in objects:
            if obj.solido and personagem.rect.colliderect(obj.rect):
                if movimento_y > 0:  # Movendo para baixo
                    personagem.rect.bottom = obj.rect.top
                if movimento_y < 0:  # Movendo para cima
                    personagem.rect.top = obj.rect.bottom

        for obj in objects:
            if not obj.solido and personagem.rect.colliderect(obj.rect):
                objects.remove(obj)

        # Preencher a tela com branco
        screen.fill(FLOOR)

        # Desenhar os objetos
        personagem.draw(screen)
        for obj in objects:
            obj.draw(screen)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        clock.tick(60)

if __name__ == "__main__":
    main()
