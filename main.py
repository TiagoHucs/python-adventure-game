import pygame
import sys
import random
from coin import Coin
from hero import Hero

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Playground RPG')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

moedas = [Coin(),Coin(),Coin(),Coin(),Coin(),Coin()]
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
    screen.fill(black)

    # Atualiza e desenha heroi
    heroi.update()
    heroi.draw(screen)

    # Desenhar moedas
    for moeda in moedas:
        moeda.draw(screen)

    # Atualizar a tela
    pygame.display.flip()

# Finalização do Pygame
pygame.quit()
sys.exit()
