import pygame
import sys
from level import levelBuilder

# Inicialize o pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Legend of Dude")
icon = pygame.image.load('assets/hero_0.png')
pygame.display.set_icon(icon)

FONT_TYPE = 'freesansbold.ttf'
FONT_SIZE = 15
font = pygame.font.Font(FONT_TYPE,FONT_SIZE)

# Definir a cor
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRASS = (0, 100, 0)

# Função principal
def main():
    clock = pygame.time.Clock()

    level = levelBuilder()
    personagem = level.getHero()
    objects = level.getObjects()
    score = 0
    
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
            movimento_x = -4
        if keys[pygame.K_RIGHT]:
            movimento_x = 4
        if keys[pygame.K_UP]:
            movimento_y = -4
        if keys[pygame.K_DOWN]:
            movimento_y = 4

        # Mover personagem e verificar colisão com objetos sólidos
        personagem.rect.x += movimento_x
        for obj in objects:
            if obj.solid and personagem.rect.colliderect(obj.rect):
                if movimento_x > 0:  # Movendo para a direita
                    personagem.rect.right = obj.rect.left
                if movimento_x < 0:  # Movendo para a esquerda
                    personagem.rect.left = obj.rect.right

        personagem.rect.y += movimento_y
        for obj in objects:
            if obj.solid and personagem.rect.colliderect(obj.rect):
                if movimento_y > 0:  # Movendo para baixo
                    personagem.rect.bottom = obj.rect.top
                if movimento_y < 0:  # Movendo para cima
                    personagem.rect.top = obj.rect.bottom

        for obj in objects:
            if not obj.solid and personagem.rect.colliderect(obj.rect):
                objects.remove(obj)
                score += 1

        # Preencher a tela com branco
        screen.fill(GRASS)

        # Desenhar os objetos
        personagem.draw(screen)
        for obj in objects:
            obj.draw(screen)

        # HUD
        text = font.render("Moedas: " + str(score), True, BLACK)
        screen.blit(text, (12,12))   
        text = font.render("Moedas: " + str(score), True, WHITE)
        screen.blit(text, (10,10))  

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        clock.tick(60)

if __name__ == "__main__":
    main()
