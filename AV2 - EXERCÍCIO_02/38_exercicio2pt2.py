'''
EXERCÍCIO 02- PARTE 02
PROFESSOR: JEIMESON ROBERTO FRANÇA
TURMA: 3º I A
ALUNO: Nicolly Gabrieli n°38
''' 

print("criptografia de cesar")
print("")

base = 'abcdefghijklmnopqrstuvwxyz'
base+= base.upper()
chave = int(input("digite a chave de griptografia\n"))

text = input("digite o texto a ser criptografado\n")

n=len(base) 

cifro = ""

for letra in text:

      indice= base.index(letra)
      nova_letra = base[(indice + chave)%n]

      cifro = cifro + nova_letra

   print("texto criptografado")
   print(cifro)