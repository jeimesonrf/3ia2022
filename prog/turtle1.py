from turtle import *

def poli(n=3,lado=100):
	for i in range(n):
		fd(lado)
		left(360/n)


if __name__ == '__main__':
	for n in range(3,100,3):
		poli(n,100)

	exitonclick()