import pygame
import sys
from level import Level
from object import Object 

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
font = pygame.font.Font(FONT_TYPE, FONT_SIZE)

# Definir a cor
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

world_map = [
    [""         , "fase1.txt", ""],
    ["fase3.txt", "fase2.txt", ""],
    [""         ,""          , ""]
]

y = 0
x = 1

# Função para carregar o nível
def load_level(y, x):
    if 0 <= y < len(world_map) and 0 <= x < len(world_map[0]):
        level = Level(world_map[y][x])
        objects = level.getObjects()
        return level, objects
    return None, []

# Função principal
def main():
    global y, x
    clock = pygame.time.Clock()

    level, objects = load_level(y, x)
    personagem = Object(100, 100, 'assets/yellow.png', solid=False)

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
        
        # Checar se mudou de fase
        
        if personagem.rect.y > screen_height:
            print('passou pra fase de baixo')
            y += 1
            personagem.rect.y = 0
        elif personagem.rect.y < 0:
            print('passou pra fase de cima')
            y -= 1
            personagem.rect.y = screen_height
        elif personagem.rect.x > screen_width:
            print('passou pra fase da direita')
            x += 1
            personagem.rect.x = 0
        elif personagem.rect.x < 0:
            print('passou pra fase da esquerda')
            x -= 1
            personagem.rect.x = screen_width

        if personagem.rect.y in [0, screen_height] or personagem.rect.x in [0, screen_width]:
            level, objects = load_level(y, x)
            if level is None:
                pygame.quit()
                sys.exit()

        screen.fill(GRAY)

        # Desenhar os objetos
        personagem.draw(screen)
        for obj in objects:
            obj.draw(screen)

        # HUD
        text = font.render("Moedas: " + str(score), True, BLACK)
        screen.blit(text, (12, 12))   
        text = font.render("Moedas: " + str(score), True, WHITE)
        screen.blit(text, (10, 10))  

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        clock.tick(60)

if __name__ == "__main__":
    main()
