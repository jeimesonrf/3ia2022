'''
EXERCÍCIO 01 - PARTE 02
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Isadora Nunes de Aquino
ALUNO: Isaque Cortina Pires
'''
alfabeto_lower = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input('Entre com a palavra a ser criptografada\n')

k_lower = int(input('Digite um número para ser o valor da chave de criptografia\n'))

k_upper = k_lower

cripto = ''

for letter in word:
        if letter in alfabeto_lower:
            position = alfabeto_lower.index(letter)
            if k_lower > 26:
                while k_lower > len(alfabeto_lower):
                    vezes = int(k_lower / len(alfabeto_lower))
                    alfabeto_lower = vezes*(alfabeto_lower + alfabeto_lower)
                    k_lower = k_lower - len(alfabeto_lower)
                    other_letter = alfabeto_lower[position + k_lower]
                    cripto += other_letter
            else:
                position = alfabeto_lower.index(letter)
                other_letter = alfabeto_lower[position + k_lower]
                cripto += other_letter
        if letter in alfabeto_upper:
            position = alfabeto_upper.index(letter)
            if k_upper > 26:     
                while k_upper > len(alfabeto_upper):
                    vezes = int(k_upper / len(alfabeto_upper))                   
                    alfabeto_upper = vezes*(alfabeto_upper + alfabeto_upper)                              
                    k_upper = k_upper - len(alfabeto_upper)
                    other_letter = alfabeto_upper[position + k_upper]
                    cripto += other_letter                                                                
            else:                                                                                         
                position = alfabeto_upper.index(letter)                                                   
                other_letter = alfabeto_upper[position + k_upper]
                cripto += other_letter
print(cripto)
