#SOLUÇÃO 1
prod = 0
count = 0
print('solução 1')
while prod < 100:
    print(f'{count:2} * 3 = {prod}')
    count += 1
    prod = count * 3

#SOLUÇÃO 2
prod = 0
count = 0
print('\nsolução 2')
while True:
    print(f'{count:2} * 3 = {prod}')
    count += 1
    prod = count * 3
    if prod >= 100:
        break
#SOLUÇÃO 3
