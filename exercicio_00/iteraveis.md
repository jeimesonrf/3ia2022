# Iteráveis

## Iteração

ato de iterar; repetição.

*iterar* : fazer ou dizer novamente; repetir.

## EM PYTHON:

A execução repetida de uma sequência de instruções é chamada de iteração (iteration). 
Como iterar é muito comum, Python tem várias características para torná-la mais fácil.

Para realizar uma repetição podemos utilizar a instrução _for_ cuja sintaxe é:

```python
for condition:
	# comandos para repetir
```
_condition_ refere-se qual tipo de iteração/repetição deseja-se.
Para e imprimirmos os números de 1 a 10 utilizaremos a função `range(initial, final, step)`, que nos criará uma lista com os números de acordo com as condições `initial`, `final` e `step`.

`initial` &rarr; número inicial  
`final` &rarr; número final  
`step` &rarr; passo, a diferença entre os números da lista

Exemplo:

`range(2,12,2)` produz a lista `[2,4,6,8,10]`

para imprimir esta lista temos o seguinte código:

```python
for i in range(2,12,2):
	print(i)
```

A variável `i` foi criada para ajudar na iteração, ela será substituída por cada item da lista.
A palavra reservada _in_ é utilizada para dizer ao interpretado de onde será retirado o valor para 
a variável.

outro exemplo:

```python
vogais = [ 'a', 'e', 'i', 'o', 'u']
for letra in vogais:
	print(letra)
```
Produz a seguinte saída:
```
a
e
i
o
u
```
Mas em Python uma string também é um iterável, então o código anterior pode ser substituído por:
```python
vogais = 'aeiou'
for letra in vogais:
	print(letra)
```
Que também produz a saída:
```
a
e
i
o
u
```

voltando ao problema do [Zenit Polar](zenit_polar.md)