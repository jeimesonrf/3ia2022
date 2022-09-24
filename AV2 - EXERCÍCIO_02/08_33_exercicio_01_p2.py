'''
EXERCÍCIOS 01 - PARTE 02
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3°IA
ALUNO: Emanuel Zanoti Rabello
ALUNO: Pedro Seijy Ogata
'''

from cgitb import reset


alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input('Entre com a primeira palavra a ser criptografada:\n')

num = int(input('Escreva quantas letras irá pular:\n'))

cripto = ''

for letter in word:
    if letter in alfabeto:
        position = alfabeto.index(letter)
        if position+num >= len(alfabeto):
            position += (num - len(alfabeto))
        else:
            position += num    
        other_letter = alfabeto[position]

        cripto += other_letter

print(cripto)