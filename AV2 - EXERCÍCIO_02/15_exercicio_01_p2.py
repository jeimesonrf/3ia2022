''' 
EXERCICIO 01 - PARTE 02
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3° I A
ALUNO: Gregory José Kolbe
ALUNO:
'''

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

k = int(input('Digite K:\n'))

cripto = ' '

for letter in alfabeto:
	if letter in alfabeto: 
		position = alfabeto.index(letter)
		if position + k >= len(alfabeto):
			position = position + k - len(alfabeto)
		else:
			position += k 
		other_letter = alfabeto[position]
		cripto += other_letter

print(cripto)