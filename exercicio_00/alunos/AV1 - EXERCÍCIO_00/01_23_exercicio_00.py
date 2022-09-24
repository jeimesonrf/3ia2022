"""ATIVIDADE REALIZADA 30/06/2022
PROFESSOR: Jeimeson
ALUNOS: Ana Beatriz Ferrer n°1 e João Henrique n°23"""


zen = "zenit"
pol = "polar"
ZEN = "ZENIT"
POL = "POLAR"

word = input ("Entre com a primeira palavra para ser criptrografada: ")

cripto = ""

for letter in word:
    if letter in zen:
       position = zen.index(letter)
       other_letter = pol [position]
       cripto += other_letter

    elif letter in pol:
       position = pol.index (letter)
       other_letter = zen[position]
       cripto += other_letter
       
    elif letter in ZEN:
        position = ZEN.index(letter)
        other_letter = POL[position]
        cripto += other_letter

    elif letter in POL:
        position = POL.index(letter)
        other_letter = ZEN [position]
        cripto += other_letter

    else:
        cripto += letter

print (cripto) 

