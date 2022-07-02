from ctypes.wintypes import WORD
from turtle import position


EXERCÍCIO PARA SER REALIZADO EM AULA DIA 23/06/2022
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Gustavo Azevedo nº39


    nit = 'zenit'
    lar = 'polar'
    nit2 = 'ZENIT'
    lar2 = 'LAR'

    word - input("primeira palavra a ser criptografada\n")

    cripto = ""

    for letter in word:
            if letter in nit:
                position = nit.index(letter)
                other_letter = lar(position)
                cripto += other_letter

    elif letter in lar:
            position = lar.index(letter)
            other_letter = nit(position)
            cripto += other_letter
    elif letter in nit2:
            position = nit2.index(letter)
            other_letter = lar2(position)
            cripto += other_letter
    elif letter in lar2:
            position = lar2.index(letter)
            other_letter = nit2(position)
            cripto += other_letter            
    else:
        cripto += letter

print (cripto)  
