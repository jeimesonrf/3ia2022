"""
EXERCÍCIO 1 07/07/2022
PROFESSOR: Jeimeson
TURMA: 3º I A
ALUNO: João Pedro Francisco Furtado
NÚMERO: 24
ALUNO: Francisco Kauan da Silva Barbosa de Miranda
NÚMERO: 12

"""

print("-=-=-=-=-=-=-Parte 01 -=-=-=-=-=-=-")
print("Criptografia de Cesar com Chave 02")
print("")

base = 'abcdefghijklmnopqrstuvwxyz'
chave = 2

text= input("Digite o texto a ser griptografado\n")
text = text.lower()
n=len(base)

cifro = ""

for letra in text:

  indice= base.index(letra)
  nova_letra = base[(indice + chave)%n]

  cifro = cifro + nova_letra

print("Texto criptografado")
print(cifro)
  