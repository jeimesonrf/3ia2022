'''
EXERCÍCIO 01 P2
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Leonardo A./27
ALUNO: Gabriel Pereira/14
'''

print ("Criptografia de Cesar")
print ("")

base = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
chave = int(input("Digite a chave de Criptografia\n"))

text= input ("Digite o texto a ser Griptografado\n")
n=len(base)

cifro = ""

for letra in text:

    indice = base.index(letra)
    nova_letra = base [(indice + chave)%n]

    cifro = cifro + nova_letra

print("Resultado")
print(cifro)