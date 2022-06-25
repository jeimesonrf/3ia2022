'''
Correção do exercício 00
professor: Jeimeson
'''
from subprocess import run, PIPE
from os import listdir

def verifica(file, termo):
	result = run(["python3", file], input=termo,stdout=PIPE)
	saida2 = result.stdout.decode('utf-8').split('\n')
	return saida2[1]

def teste(exercicio, palavras):
	saida = []
	for f in listdir():
		tamanho = len(exercicio)
		if exercicio in f :
			if len(f) == tamanho+3:
				numero_1 = f[0:2]
				numero_2 = '  '
			else:
				numero_1 = f[0:2]
				numero_2 = f[3:5]
			with open(palavras,'r') as dados:
				linhas = dados.readlines()
				soma = 0
				for linha in linhas:
					linha = linha.strip('\n').split(',')
					termo = bytes(linha[0],'utf-8')
					resp = linha[1]
					teste = verifica(f, termo)
					if teste == resp:
						soma += 1
			saida.append([numero_1, numero_2 ,soma])
	return saida

def main():
	alunos = teste('exercicio_00.py', 'dados.txt')
	for aluno in alunos:
		print(aluno)

if __name__ == '__main__':
	main()