'''
EXERCÍCIO PARA SER REALIZADO EM AULA DIA 30/06/2022
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º IA
ALUNO:Leonardo Antonio de Oliveira Beltrão / n°27
ALUNO:Gabriel  Pereira de Faria / n°14
'''

zenit = 'zenit'

polar = 'polar'

ZENIT = 'ZENIT'

POLAR = 'POLAR'

word = input ('Entre com palavra a ser criptografada \n')

cripto = ''

for letter in word :
    if letter in zenit :
        position = zenit.index (letter)
        other_letter = polar [position]
        cripto += other_letter

    elif letter in polar :

        position = polar.index (letter)
        other_letter = zenit [position]
        cripto += other_letter

    elif letter in ZENIT :

        position = ZENIT.index (letter)
        other_letter = POLAR [position]
        cripto += other_letter

    elif letter in POLAR :

        position = POLAR.index (letter)
        other_letter = ZENIT [position]
        cripto += other_letter

    else :
            cripto += letter
print (cripto)
