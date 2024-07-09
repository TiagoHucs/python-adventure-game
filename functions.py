from object import Object 
from level import Level 

def levelBuilder():
    objects = []

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
                objects.append(Object(indice_caractere*32, indice_linha*32, 'assets/wall_0.png', solido=True))
            elif caractere == 'H':
                personagem = Object(indice_caractere*32, indice_linha*32, 'assets/hero_0.png', solido=False)
                #level.append(personagem)
            elif caractere == 'T':
                objects.append(Object(indice_caractere*32, indice_linha*32, 'assets/tree_0.png', solido=True))
            elif caractere == 'C':
                objects.append(Object(indice_caractere*32, indice_linha*32, 'assets/coin_0.png', solido=False))

    level1 = Level(personagem, objects)
    return level1