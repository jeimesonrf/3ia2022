'''
EXERCÍCIO 01 - PARTE 02
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: ANDRIELI LUCI GONÇALVES
ALUNO:
'''

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# representa quantas "casas" serão avançadas, conforme a posição das letras no alfabeto
k = int(input('Qual quantidade de posições você deseja pular?\n'))

# campo para receber a palavra
word = input('Qual palavra deseja criptografar?\n')

# variável que dará origem à palavra criptografada
cripto = ''

# estrutura de repetição que analisará cada letra da palavra recebida
for letter in word:

    # caso "letter" não exista em "word", "letter" é apenas adicionado à variável "cripto"
    if (letter not in alfabeto):
        cripto += letter

    # caso contrário, os comandos abaixo são executados
    else:

        ''' 
        -> estrutura de repetição para cada caractere da variável "alfabeto"
        -> são 52 caracteres, pois o alfabeto está duplicado (maiúsculas e minúsculas)
        '''
        for i in range(0, 52):
        
            ''' 
            -> verifica se a letra de "word" corresponde a letra atual do alfabeto
            ->  se falso, passa-se para a próxima posição do alfabeto
            '''
            if (letter == alfabeto[i]):
                
                # a nova posição será igual ao valor de k somado à posição da letra atual do alfabeto
                position = i + k
                
                ''' 
                faz com que a nova posição se restrinja apenas ao alfabeto em que a letra de "word" se encaixa, ou seja,
                minúsculas só terão correspondentes minúsculas, enquanto maiúsculas, apenas maiúsculas.
                '''
                if (i <= 25 and position >= 25 or i >= 26 and position > 51):
                    position -= 26 # retira 26 caracteres
                    
                # criação da nova letra    
                new_letter = alfabeto[position]

                # concantenando a nova letra à variável da palavra criptografada
                cripto += new_letter
            
print(cripto)