'''
EXERCÍCIO 01 
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: isabeli vitoria lopes barbosa n°19
ALUNO: beatriz nelos n°05
'''                 


chave = int(input("digite a chave de criptografia (ate 26)\n"))
while chave > 26 or chave < 0:  
    print(" ")
    chave = input("chave inválida, tente novamente")
base = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
text= input("Digite o texto a ser criptografado\n")
cripto =''
if ('encriptar') :
    for word in text:             
        posicion = base.find(word)           
        posicion += chave        
        if(posicion > len(base)):
            posicion = posicion - len(base)       
        cripto = cripto + base[posicion]

print("sua mensagem \n" + cripto)