"""
EXERCÍCIO 0 23/06/2022
PROFESSOR: Jeimeson
TURMA: 3º I A
ALUNO: João Pedro Francisco Furtado
NÚMERO: 24
ALUNO: Francisco Kauan da Silva Barbosa de Miranda
NÚMERO: 12

"""
zenit= 'zenit'
polar = 'polar'
ZENIT= 'ZENIT'
POLAR= 'POLAR'
word = input('Escreva a palavra que quiser ser criptografada\n')

cripto = ''

for letter in word:

    if letter in zenit:

        position = zenit.index(letter)

        other_letter = polar [position]

        cripto += other_letter

    elif letter in polar:

        position = polar.index(letter)

        other_letter = zenit [position]

        cripto += other_letter

    elif letter in ZENIT:

        position = ZENIT.index(letter)

        other_letter = POLAR [position]

        cripto += other_letter 

    elif letter in POLAR:

        position = POLAR.index(letter)

        other_letter = ZENIT [position]

        cripto += other_letter       

    else:
         cripto += letter 

print(cripto)