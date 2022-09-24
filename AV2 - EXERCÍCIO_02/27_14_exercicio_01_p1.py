'''
EXERCÍCIO 01 - PARTE 01
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Leonardo A./27
ALUNO: Gabriel Pereira/14
'''
print ("Criptografia de Cesar")
print ("")

base = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
chave = 2

text= input ("Digite o texto a ser Griptografado\n")
n=len(base)

cifro = ""

for letra in text:

    indice = base.index(letra)
    nova_letra = base [(indice + chave)%n]

    cifro = cifro + nova_letra

print("Resultado")
print(cifro)
