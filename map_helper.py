def load_world_map(filename):
    world_map = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove espaços e quebras de linha no final de cada linha
            line = line.strip()
            # Divide a linha em elementos, separando por vírgula
            row = [item.strip() for item in line.split(',')]
            # Adiciona a linha à matriz
            world_map.append(row)
    return world_map

#filename = 'world_map.txt'
#world_map = load_world_map(filename)
#print(world_map)