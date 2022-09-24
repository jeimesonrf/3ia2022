'''
EXERCÍCIO 01 - PARTE 01
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º IA
ALUNO: Emanuel Zanoti Rabello
ALUNO: Pedro Seijy Ogata
'''
alfabeto1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto2 = 'cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB'

word = input('Entre com a primeira palavra a ser criptografada\n')

cripto = ''

for letter in word:
    if letter in alfabeto1:
        position = alfabeto1.index(letter)    
        other_letter = alfabeto2[position]
        cripto += other_letter

print (cripto)
        