'''
EXERCÍCIO 01 - PARTE 02
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Tiago Hilgenberg Ijaille Budziak
ALUNO:
'''
alfabeto = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

# qtnd de letras que serão puladas
k = int(input('Digite K:\n'))

# enquanto a qtnd de letras puladas for maior ou menor que a qtnd de letras no alfabeto
while k > 26 or k < 0:
    # indique que k é inválido e digite de novo
    print('Valor de K inválido. Digite novamente:')
    # valor de k
    k = int(input(''))

# ler a palavra a ser criptografada
word = input('Entre com a palavra a ser criptografada\n')

# criar uma palavra vazia que receberá a criptografia
cripto = ''


# para cada letra na palavra
for letter in word:
    # se a letra for minúsucla
    if letter.islower():
        # verificar se está na chave minúscula
        if letter in alfabeto:
            # se estiver na chave pegar a posição da letra
            position = alfabeto.index(letter)
            # e pegar a letra correspondente a mesma posição na outra chave
            other_letter = alfabeto[position + k]
            #acrescentar esta letra na palavra criptografada
            cripto += other_letter
        # o espaço não está na chave então repetimos
        else:
            cripto += letter
    # se a chave for maiúscula
    else:
         # verificar se está na chave maiúscula
        if letter in ALFABETO:
        # se estiver na chave pegar a posição da letra
            position = ALFABETO.index(letter)
        # e pegar a letra correspondente a mesma posição na outra chave
            other_letter = ALFABETO[position + k]
        #acrescentar esta letra na palavra criptografada
            cripto += other_letter
        # o espaço não está na chave então repetimos
        else:
            cripto += letter

# imprima a saída
print(cripto)
