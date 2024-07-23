from object import Object 

class Level:
    def __init__(self, file_name):
        print('criando:', file_name)
        self.objects = []

        with open('maps/'+file_name+'.txt', 'r') as file:
            lines = file.readlines()

        for line_index, line in enumerate(lines):
            items = line.split()  # Divide a linha em itens separados por espaços
            for col_index, item in enumerate(items):
                if item == '00':
                    self.objects.append(Object(col_index*32, line_index*32, 'assets/black.png', solid=True))
                elif item == 'RR':
                    self.objects.append(Object(col_index*32, line_index*32, 'assets/red.png', solid=True))
                elif item == 'YY':
                    self.objects.append(Object(col_index*32, line_index*32, 'assets/yellow.png', solid=True))
                elif item == 'yy':
                    self.objects.append(Object(col_index*32, line_index*32, 'assets/yellow.png', solid=False))
                elif item == 'GG':
                    self.objects.append(Object(col_index*32, line_index*32, 'assets/green.png', solid=True))
                elif item == 'BB':
                    self.objects.append(Object(col_index*32, line_index*32, 'assets/blue.png', solid=True))
                elif item == 'DD':
                    self.objects.append(Object(col_index*32, line_index*32, 'assets/dragon0.png', solid=True))

        print('fim da criacao:', file_name)

    def getObjects(self):
        return self.objects