'''
EXERCÍCIO PARA SER REALIZADO EM AULA DIA 23/06/2022
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: ANDRIELI LUCI GONÇALVES
ALUNO:
'''

word = input('Entre com a palavra a ser criptografada\n')
cripto = ''

for letter in word:

    zenit = 'zenit'
    polar = 'polar'
    concatenated_letter = False # estabelece se uma nova letra foi ou não concatenada

    while concatenated_letter == False:
        
        if letter in zenit:
            position = zenit.index(letter)
            other_letter = polar[position]
            cripto += other_letter
            concatenated_letter = True # letra foi concatenada à palavra criptografada

        elif letter in polar:
            position = polar.index(letter)
            other_letter = zenit[position]
            cripto += other_letter
            concatenated_letter = True # letra foi concatenada à palavra criptografada

        elif letter in zenit.upper() or letter in polar.upper():
            zenit = zenit.upper()
            polar = polar.upper()

        else:
            cripto += letter
            concatenated_letter = True # letra foi concatenada à palavra criptografada

# imprimindo a saída
print(cripto)