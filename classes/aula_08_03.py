class Cachorro():

    # atributos
    nome = ''
    tutor = ''
    idade = 0
    raca = ''
    porte = ''
    peso = 0.0 # 0. .0

    def __init__(self, nome_pet, tutor_pet): # Construtor
        nome = 'Jojo' # variavel que só vale dentro da função __init__
        self.nome = nome_pet # atributo da classe
        self.tutor = tutor_pet
    
    def comer(self):
        print(f'O pet {self.nome} está comendo')

    def dormir(self):
        print(f'O pet {self.nome} está dormindo')
    
    def latir(self):
        print(f'Au au, {self.nome} latiu')


if __name__ == '__main__':
    leia = Cachorro('Leia', 'Jeimeson')
    cristal = Cachorro('Cristal', 'Emanuel')

    leia.comer()
    print(leia.tutor)
    cristal.latir()
    print(cristal.tutor)