import time

number01 = int(input("What's the first number?\n").strip())
number02 = int(input("What's the second number?\n").strip())
choose = 0

while choose != 5 :
    choose = int(input('\033[1:36mWhat we do with the numbers?\033[m\n'
                       '[1] = SUM\n'
                       '[2] = MULTIPLY\n'
                       '[3] = BIGGEST NUMBER\n'
                       '[4] = NEW NUMBERS\n'
                       '[5] = END PROGRAM\n'))

    if choose == 1 :
        sum = number02 + number01
        time.sleep(2)
        print(f'The result of sum of the number {number01} and {number02} is {sum}')

    elif choose == 2 :
        multiply = number02 * number01
        time.sleep(2)
        print(f'The multiply of the number {number01} and {number02} is {multiply}')

    elif choose == 3 :
        if number01 > number02 :
            print(f'The biggest number is {number01}')

        else :
            print(f'The biggest number is {number02}')

    elif choose == 4 :
        print('Write a numbers again :')
        number01 = int(input("What's the first number?\n").strip())
        number02 = int(input("What's the second number?\n").strip())

    elif choose < 1 and choose > 5 :
        print('\033[1:31mDo a right choose!!\033[m')

print('Ending...')
time.sleep(0.5)
print('\033[1:31mEnd of the program...')
