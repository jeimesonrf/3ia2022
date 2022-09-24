'''
EXERCÍCIO 01 - PARTE 02
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO:Leonardo Sotti Pinhelli
ALUNO:
'''
#recebe a chave de critografia e valida
chave = int(input("digite a chave de criptografia (ate 26)\n"))
while chave > 26 or chave < 0:  
    print(" ")
    chave = input("chave inválida, tente novamente")

base = 'abcdefghijklmnopqrstuvwxyz'

#escolhe o modo
modo = str(input("Deseja encriptar ou descriptar\n"))

#insere e formata o texto
text= input("Digite o texto a ser criptografado\n")
text = text.lower()


#insere o texto final
cripto =''

    #escolhe o modo
if (modo == 'e' or modo == 'encriptar') :
    for word in text:
                #encontra o numero da posição dp word na base
        posicion = base.find(word)

            #soma a chave á posição
        posicion += chave

            # se a posição for maior que a base ira calcular a diferença
        if(posicion > len(base)):
            posicion = posicion - len(base)

    #concatena a o word encontrado           
        cripto = cripto + base[posicion]

elif (modo == 'd' or modo == 'decriptar'):
        # contador do texto
            # recebe o word da posição
            #condição se o word estiver contido na base
    for word in text:
            #encontra a posição
        posicion = base.find(word)
            #subtrai a chave
        posicion -= chave
            #condicional se a posição foi menor que 0
        if posicion < 0:
                # subtrai o valor absoluto da base para encontrar a posição
            posicion = len(base)- abs(posicion)

    #resultado            
        cripto = cripto + base[posicion]

print("sua mensagem \n" + cripto)