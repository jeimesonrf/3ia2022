'''
EXERCÍCIOS 01 - PARTE 01
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3°IA
ALUNO: Emanuel Zanoti Rabello
ALUNO: Pedro Seijy Ogata
'''
alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input('Entre com a primeira palavra a ser criptografada:\n')

num = 2

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