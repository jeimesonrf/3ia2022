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

def teste(exercicio, palavras,path):
	saida = {}
	for f in listdir(path):
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
					try:
						teste = verifica(path+f, termo)
						if teste == resp:
							soma += 1
					except:
						print(f,soma)
						soma += 0
			saida.update({numero_1:soma})
			if numero_2 != '  ':
				saida.update({numero_2:soma})
	return saida

def main():
	path = 'alunos/AV1 - EXERCÍCIO_00/'
	alunos = teste('exercicio_00.py', 'dados.txt',path)
	print(alunos)
	with open('saida.txt', 'w'):
		pass
	with open('saida.txt','a') as f:
		for aluno in sorted(alunos):
			print(aluno,alunos[aluno])
			f.writelines(aluno+','+str(alunos[aluno])+'\n')

if __name__ == '__main__':
	main()