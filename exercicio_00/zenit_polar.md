1. Ler a palavra para criptografar
2. Verificar cada letra da palavra nas chaves
3. Se existe a letra na chave, pego a letra correspondente na outra chave
4. Se não existe repito a letra
5. Imprimir a palavra codificada

Em Python

```python
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
```
Verificando a execução no arquivo [zenit_polar.py](zenit_polar.py)

E depois vamos ao exercício de hoje: [exercício](exercício.md)