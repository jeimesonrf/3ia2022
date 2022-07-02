'''
EXERCÍCIO PARA SER REALIZADO EM AULA DIA 23/06/2022
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º IA
ALUNO: EMANUEL ZANOTI RABELLO
ALUNO: PEDRO SEIJY OGATA
'''

print(32*'=', '\n | CRIPTOGRAFANDO UMA PALAVRA | \n'+ 32*'=')

zenit_lower = 'zenit'
polar_lower = 'polar'
zenit_upper = 'ZENIT'
polar_upper = 'POLAR'

word = input('Entre com a primeira palavra a ser criptografada\n')

cripto = ''

for letter in word:
    if letter in zenit_lower:
        position = zenit_lower.index(letter)    
        other_letter = polar_lower[position]
        cripto += other_letter

    elif letter in polar_lower:
        position = polar_lower.index(letter)    
        other_letter = zenit_lower[position]
        cripto += other_letter
        
    elif letter in zenit_upper:
        position = zenit_upper.index(letter)    
        other_letter = polar_upper[position]
        cripto += other_letter

    elif letter in polar_upper:
        position = polar_upper.index(letter)    
        other_letter = zenit_upper[position]
        cripto += other_letter    
    else:
        cripto += letter

print (cripto)