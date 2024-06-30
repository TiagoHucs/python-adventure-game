import pygame
import sys
from coin import Coin
from hero import Hero

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'Playground RPG 2'
FONT_TYPE = 'freesansbold.ttf'
FONT_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0 , 0 , 0)
RED = (255,0,0)

# Inicialização do Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
font = pygame.font.Font(FONT_TYPE,FONT_SIZE)


points = 0

moedas = [Coin(),Coin(),Coin(),Coin(),Coin()]
moedas.append(Coin())
heroi = Hero()

# Loop principal
running = True
while running:

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            heroi.trate_event(event)

    # Limpar a tela
    screen.fill(BLACK)

    # Atualiza e desenha heroi
    heroi.update()
    heroi.draw(screen)

    # Desenhar moedas
    for moeda in moedas:
        moeda.draw(screen)
        if moeda.rect.colliderect(heroi.rect):
            pygame.draw.rect(screen, RED, heroi.rect, 2)
            moedas.remove(moeda)
            points += 1


    text = font.render("Moedas: " + str(points), True, WHITE)
    screen.blit(text, (10,10))

    # Atualizar a tela
    pygame.display.flip()

# Finalização do Pygame
pygame.quit()
sys.exit()
