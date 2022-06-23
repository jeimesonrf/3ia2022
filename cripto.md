# Criptografia

Conjunto de princípios e técnicas para cifrar a escrita, 
torná-la ininteligível para os que não tenham acesso às convenções combinadas; 

---
## Simples troca

### Zenit Polar

---
<center>
Z E N I T

P O L A R
</center>

Substitui-se a letra presente numa palavra pela correspondente na outra palavra.
Por exemplo: C A N E T A  

| Letra  | corresponde  | Cripto  |
|:-:|:-:|:-:|
| C  | não tem  | C  |
| A  | I  | I  |
| N  | L  | L  |
| E | O | O |
| T | R | R |
| A | I | I |

---
Vamos implementar um algoritmo para fazer a cifragem ZENIT/POLAR


1. Ler a palavra para criptografar
2. Verificar cada letra da palavra nas chaves
3. Se existe a letra na chave, pego a letra correspondente na outra chave
4. Se não existe repito a letra
5. Imprimir a palavra codificada

---
Próximo passo é implementar numa linguagem de programação para transformar o algoritmo
em um programa. Vamos faze-lo em PYTHON.

[Vamos ao Python](iteraveis.md)