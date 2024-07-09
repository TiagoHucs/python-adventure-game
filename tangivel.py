import pygame
import sys

# Inicialize o pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Projeto com Quadrados Tangíveis e Intangíveis")

# Definir a cor
white = (255, 255, 255)
BLACK = (0, 0, 0)
FLOOR = (0, 100, 0)

# Classe Objeto
class Objeto:
    def __init__(self, x, y, image_path, solido=True):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.solido = solido

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

# Função principal
def main():
    clock = pygame.time.Clock()

    # Criar objetos
    personagem = Objeto(100, 100, 'assets/hero/hero_0.png', solido=False)
    arvore1 = Objeto(400, 200, 'assets/tree_0.png', solido=True)
    arvore2 = Objeto(500, 450, 'assets/tree_0.png', solido=True)
    moeda = Objeto(300, 500, 'assets/coin/coin_0.png', solido=False)

    objetos = []

    # Nome do arquivo que será lido
    nome_arquivo = "fase1.txt"
    
    # Abre o arquivo para leitura da fase
    with open(nome_arquivo, 'r') as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

    # Percorre cada linha com seu índice
    for indice_linha, linha in enumerate(linhas):
        # Percorre cada caractere na linha com seu índice
        for indice_caractere, caractere in enumerate(linha):
            # Realiza uma ação com o índice da linha, o índice do caractere e o caractere
            if caractere == '0':
                objetos.append(Objeto(indice_caractere*32, indice_linha*32, 'assets/wall_0.png', solido=True))
            elif caractere == 'H':
                personagem = Objeto(indice_caractere*32, indice_linha*32, 'assets/hero/hero_0.png', solido=False)
                objetos.append(personagem)
            elif caractere == 'T':
                objetos.append(Objeto(indice_caractere*32, indice_linha*32, 'assets/tree_0.png', solido=True))
            elif caractere == 'C':
                objetos.append(Objeto(indice_caractere*32, indice_linha*32, 'assets/coin/coin_0.png', solido=False))

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
        for obj in objetos:
            if obj.solido and personagem.rect.colliderect(obj.rect):
                if movimento_x > 0:  # Movendo para a direita
                    personagem.rect.right = obj.rect.left
                if movimento_x < 0:  # Movendo para a esquerda
                    personagem.rect.left = obj.rect.right

        personagem.rect.y += movimento_y
        for obj in objetos:
            if obj.solido and personagem.rect.colliderect(obj.rect):
                if movimento_y > 0:  # Movendo para baixo
                    personagem.rect.bottom = obj.rect.top
                if movimento_y < 0:  # Movendo para cima
                    personagem.rect.top = obj.rect.bottom

        for obj in objetos:
            if not obj.solido and personagem.rect.colliderect(obj.rect):
                objetos.remove(obj)

        # Preencher a tela com branco
        screen.fill(FLOOR)

        # Desenhar os objetos
        personagem.draw(screen)
        for obj in objetos:
            obj.draw(screen)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        clock.tick(60)

if __name__ == "__main__":
    main()
