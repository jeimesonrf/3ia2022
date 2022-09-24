from turtle import *
def square(tamanho):
    for i in range(4):
        forward(tamanho)
        left(90)

        
def poligono(numero_lados, tamanho):
    """
    numero_lados : int
        numero de lados do poligono
    tamanho : int
        comprimento do lado do poligono
    """
    angulo = 360 / numero_lados
    for i in range(numero_lados):
        forward(tamanho)
        left(angulo)
        
def outro():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
done()


if __name__ == '__main__':
	outro()