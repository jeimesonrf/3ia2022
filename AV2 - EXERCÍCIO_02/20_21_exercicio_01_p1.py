'''
EXERCÍCIO 01 - PARTE 01
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Isadora Nunes de Aquino
ALUNO: Isaque Cortina Pires
'''
alfabeto = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input('Entre com a palavra a ser criptografada\n')

k = 2

cripto = ''

for letter in word:
    if letter in alfabeto:
        position = alfabeto.index(letter)
        other_letter = alfabeto[position + k]
        cripto += other_letter
    else:
        cripto += letter
print(cripto)
