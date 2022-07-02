'''
EXERCÍCIO PARA SER REALIZADO EM AULA DIA 23/06/2022
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO:Gustavo Garcias 
ALUNO:Vitor B.
'''

# criar as variáveis com as chaves da criptografia
zenit = 'zenit'
polar = 'polar'
POLAR = 'POLAR'
ZENIT = 'ZENIT'
# ler a palavra a ser criptografada
word = input('Entre com a palavra a ser criptografada\n')

# criar uma palavra vazia que receberá a criptografia
cripto = ''

# para cada letra na palavra
for letter in word:
	# verificar se está na chave
	if letter in zenit:
		# se estiver na chave pegar a posição da letra
		position = zenit.index(letter)
		# e pegar a letra correspondente a mesma posição na outra chave
		other_letter = polar[position]
		#acrescentar esta letra na palavra criptografada
		cripto += other_letter
	# também devemos verificar a letra na outra chave
	elif letter in polar:
		# se estiver na chave pegar a posição da letra
		position = polar.index(letter)
		# e pegar a letra correspondente a mesma posição na outra chave
		other_letter = zenit[position]
		#acrescentar esta letra na palavra criptografada
		cripto += other_letter
	# se não estiver em nenhuma chave, apenas repetimos a letra
	

   
   # para cada letra na palavra
for letter in word:
	# verificar se está na chave
	if letter in ZENIT:
		# se estiver na chave pegar a posição da letra
		position = ZENIT.index(letter)
		# e pegar a letra correspondente a mesma posição na outra chave
		other_letter = POLAR[position]
		#acrescentar esta letra na palavra criptografada
		cripto += other_letter
	# também devemos verificar a letra na outra chave
	elif letter in POLAR:
		# se estiver na chave pegar a posição da letra
		position = POLAR.index(letter)
		# e pegar a letra correspondente a mesma posição na outra chave
		other_letter = ZENIT[position]
		#acrescentar esta letra na palavra criptografada
		cripto += other_letter
	# se não estiver em nenhuma chave, apenas repetimos a letra
	
# imprimindo a saída
print(cripto)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   