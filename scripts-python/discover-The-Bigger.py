import time

program = True

'''def biggestNumber(numbersList, totalValues) :
    numbersList.sort()
    print('Validating the informed numbers...')
    time.sleep(1)
    print(f"The biggest number is {numbersList[-1]} and informed {totalValues} numbers")

allNumbers = []
valuesInformed = 0

while program :
    number = int(input('Write a number to add in numbers list : \n').strip())
    allNumbers.append(number)
    valuesInformed += 1

    choose = str(input('You want continue? [\033[1:32mY\033[m]/[\033[1:31mN\033[m]')).strip().upper()

    while choose != 'N' and choose != 'Y' :
        print('\033[1:31mChoose a right decision!!\033[m')
        choose = str(input('You want continue? [\033[1:32mY\033[m]/[\033[1:31mN\033[m]')).strip().upper()


    if choose == 'N' :
        break

biggestNumber(allNumbers, valuesInformed)'''

def biggestNumber(*numbers) :
    counter = biggest = 0
    print('Values in analysis...')
    time.sleep(1)

    if not numbers :
        print('The biggest number is 0...')

    else :
        for number in numbers :
            print(f"{number}", end='; ')
            if biggest == 0 :
                biggest = number

            else :
                if number > biggest :
                    biggest = number

            time.sleep(0.3)
        print()
        time.sleep(0.5)

        print('The biggest number of the sequence [', end='')
        for number in numbers :
            print(f"{number}", end=';')

        print(']', end=' ')
        print(f'is {biggest}')



biggestNumber(1, 6, 4, 2)
biggestNumber(2, 7)
biggestNumber(1)
biggestNumber()