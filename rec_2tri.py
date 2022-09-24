n = int(input('Qual o limite?'))
for i in range(1,n+1):
	if (i % 7 == 0) or (i % 10 == 7):
		print('pim', end = ' - ')
	else:
		print(i, end = ' - ')
print()
	