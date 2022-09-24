print("criptografia de cesar")
print("")

base = 'abcdefghijklmnopqrstuvwxyz'
base+= base.upper()
chave = int(input("digite a chave de criptografia\n"))

text = input("digite o texto a ser criptografado\n")

n=len(base) 

cifro = ""

for letra in text:

      indice= base.index(letra)
      nova_letra = base[(indice + chave)%n]

      cifro = cifro + nova_letra

print("texto criptografado")
print(cifro)
