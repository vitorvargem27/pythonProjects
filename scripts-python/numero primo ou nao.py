num = int(input('Digite um número\n'))
total = 0 #número de vezes que o número foi dividido que começa em zero

for x in range(1, num + 1 ) :
    if num % x == 0 : # verificando se o número é divisivel apenas por ele mesmo
        print('\033[32m')
        total += 1

    else:
        print('\033[31m')

    print(x, end = ' ')

print(f'\n\nO número {num} foi dividido {total} vezes')

if total == 2 :
    print('O número é primo')

else :
    print('O numero não é primo')
