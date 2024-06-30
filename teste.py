import pygame
import sys

# Inicialize o pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Teste de Colisão entre Quadrados")

# Definir a cor
white = (255, 255, 255)
black = (0, 0, 0)

# Classe Quadrado
class Quadrado:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

# Função principal
def main():
    clock = pygame.time.Clock()

    # Criar dois objetos quadrados
    quadrado1 = Quadrado(100, 100, 50, 50, black)
    quadrado2 = Quadrado(300, 200, 50, 50, black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Movimentar o primeiro quadrado com as setas do teclado
        if keys[pygame.K_LEFT]:
            quadrado1.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            quadrado1.move(5, 0)
        if keys[pygame.K_UP]:
            quadrado1.move(0, -5)
        if keys[pygame.K_DOWN]:
            quadrado1.move(0, 5)

        # Verificar colisão
        if quadrado1.rect.colliderect(quadrado2.rect):
            print("Colisão detectada!")

        # Preencher a tela com branco
        screen.fill(white)

        # Desenhar os quadrados
        quadrado1.draw(screen)
        quadrado2.draw(screen)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        clock.tick(30)

if __name__ == "__main__":
    main()
