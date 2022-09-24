# criar as variáveis com as chaves da criptografia
zenit = 'zenit'
polar = 'polar'

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
	else:
		cripto += letter
# imprimindo a saída
print(cripto)
