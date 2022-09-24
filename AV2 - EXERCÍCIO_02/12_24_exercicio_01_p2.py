"""
EXERCÍCIO 1 07/07/2022
PROFESSOR: Jeimeson
TURMA: 3º I A
ALUNO: João Pedro Francisco Furtado
NÚMERO: 24
ALUNO: Francisco Kauan da Silva Barbosa de Miranda
NÚMERO: 12

"""

print("-=-=-=-=-=-=-Parte 02 -=-=-=-=-=-=-")
print("Criptografia de Cesar ")
print("")

base = 'abcdefghijklmnopqrstuvwxyz'
base += base.upper()
chave = int(input("digite a chave de criptografia\n"))

text= input("Digite o texto a ser griptografado\n")

n=len(base)

cifro = ""

for letra in text:

  indice= base.index(letra)
  nova_letra = base[(indice + chave)%n]

  cifro = cifro + nova_letra

print("Texto criptografado")
print(cifro)
  
  
  