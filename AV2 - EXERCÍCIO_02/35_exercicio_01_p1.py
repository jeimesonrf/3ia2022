'''
EXERCÍCIO 01 - PARTE 01
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Tiago Hilgenberg Ijaille Budziak
ALUNO:
'''
alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
k2 = 'cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB'

# ler a palavra a ser criptografada
word = input('Entre com a palavra a ser criptografada\n')

# criar uma palavra vazia que receberá a criptografia
cripto = ''

# para cada letra na palavra
for letter in word:
    # verificar se está na chave
    if letter in alfabeto:
        # se estiver na chave pegar a posição da letra
        position = alfabeto.index(letter)
        # e pegar a letra correspondente a mesma posição na outra chave
        other_letter = k2[position]
        #acrescentar esta letra na palavra criptografada
        cripto += other_letter
    else:
        cripto += letter

# imprimindo a saída
print(cripto)