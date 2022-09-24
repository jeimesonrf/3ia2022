'''
EXERCÍCIO PARA SER REALIZADO EM AULA DIA 23/06/2022
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Sthefany Kamila Machado
ALUNO:
'''
# criar as variáveis com as chaves da criptografia
zenit = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' 
polar = 'd,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a,b,c'
zenit += zenit.upper()
polar += polar.upper()
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
		# para cada letra na palavra

# imprimindo a saída
print(cripto)
