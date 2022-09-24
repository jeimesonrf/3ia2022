class Aluno():

    nome = ''
    endereco = ''
    pai = ''
    mae = ''
    rg = ''

    def __init__(self,nome, mae):
        self.nome = nome
        self.mae = mae
    
    def estudar(self):
        print('O aluno ',self.nome,' foi estudar.')

class Estudante():

    def estudar(self):
        print('Não perturbe, estou estudando.')