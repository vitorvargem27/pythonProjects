numberTuple = ()
pairTuple = ()
timesNumber09 = 0

for x in range (0, 4) :
    number = int(input('Write a number to add in number list :\n').strip())
    numberTuple += (number,) #escrito dessa maneira para inserir na tupla
    if number == 9 :
        timesNumber09 += 1

    if number % 2 == 0 :
        pairTuple += (number,)

print(f'You wrote the numbers : \033[1:36m{numberTuple}\033[m')
print(f'The time of appears of the number 9 is \033[1:35m{timesNumber09}\033[m')

if 3 in numberTuple :
    print(f'The number 3 is in the position {numberTuple.index(3) + 1}°')

else :
    print('Do not have a number 3')

print(f'The pair numbers wrote is :', end=' ' )
for pair in (sorted(pairTuple)) :
    print(f'{pair}', end=' ')
