class Classe1 :

	ordem = 0

	def __init__(self):
		Classe1.ordem+=1

	@property
	def _ordem(self):
		return Classe1.ordem

if __name__ == '__main__':
	c1 = Classe1()
	print(c1.ordem)
	c2 = Classe1()
	c4 = Classe1()
	c5 = Classe1()
	c6 = Classe1()
	c7 = Classe1()
	print(c2.ordem)
