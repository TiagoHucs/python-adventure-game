from object import Object 

class Level:
    def __init__(self, file_name):
        print('criando:', file_name)
        self.objects = []

        with open('maps/'+file_name+'.txt', 'r') as file:
            lines = file.readlines()

        for line_index, line in enumerate(lines):
            for col_index, caractere in enumerate(line):
                if caractere == '0':
                    self.objects.append(Object(col_index*32, line_index*32, 'assets/blue.png', solid=True))
        print('fim da criacao:', file_name)

    def getObjects(self):
        return self.objects