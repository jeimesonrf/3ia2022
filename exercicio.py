class Gato():

	def __init__ (self, nome): 
		self.nome = nome
		self.idade = 0
		self.raca = ''
	
	def miar(self):
		print(f'O {self.nome} está miando')
	
	def comer(self):
		print(f'O {self.nome} está comendo')

	def dormir(self):
		print(f'O {self.nome} está dormindo')

def operacoes(n1, n2):
	print(n1+n2)
	print(n1-n2)

def produto(n1, n2):
	return n1*n2


if __name__ == '__main__':

	yoda = Gato('Yoda')

	yoda.miar()
	yoda.comer()
	yoda.dormir()

	operacoes(1,1)
	print(produto(2,3))