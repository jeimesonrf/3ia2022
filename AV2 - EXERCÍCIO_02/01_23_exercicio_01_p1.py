
'''EXERCÍCIOS 01 - PARTE 01
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3°IA
ALUNO: Ana Beatriz Ferrer
ALUNO: João Henrique
'''
alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input('Entre com a primeira palavra a ser criptografada:\n')

chave = 2

cripto = ''

for letter in word:
    if letter in alfabeto:
        position = alfabeto.index(letter)
        if position+chave >= len(alfabeto):
            position += (chave - len(alfabeto))
        else:
            position += chave
        other_letter = alfabeto[position]
        cripto += other_letter

print(cripto)