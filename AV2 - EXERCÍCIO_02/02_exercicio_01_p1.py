'''
EXERCÍCIO 01 - PARTE 01
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: ANDRIELI LUCI GONÇALVES
ALUNO:
'''

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# representa quantas "casas" serão avançadas, conforme a posição das letras no alfabeto
k = 2 

# campo para receber a palavra
word = input('Qual palavra deseja criptografar?\n') 

# variável que dará origem à palavra criptografada
cripto = '' 

# estrutura de repetição que analisará cada letra da palavra recebida
for letter in word:

    # verifica se "letter" encontra-se em "alfabeto"
    if (letter in alfabeto):
        position = alfabeto.index(letter) # busca pela posição da letra no "alfabeto"
        new_position = position + k # altera a posição conforme o valor de "k"

        ''' 
        faz com que a nova posição se restrinja apenas ao alfabeto em que a letra de "word" se encaixa, ou seja,
        minúsculas só terão correspondentes minúsculas, enquanto maiúsculas, apenas maiúsculas.
        '''
        if (position <= 25 and new_position >= 25 or position >= 26 and new_position > 51):
            new_position -= 26 

        # criação da nova letra    
        new_letter = alfabeto[new_position]

        # concantenando a nova letra à variável da palavra criptografada
        cripto += new_letter
    # comando executado quando "letter" não está em "alfabeto"
    else:
        cripto += letter # concatena à variável "cripto" a letra original digitada pelo usuário
            
print(cripto)