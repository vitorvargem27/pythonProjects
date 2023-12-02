import random
import time

win = True
count = 0
while win :
    machine = random.randint(1, 10)
    print('Options for start game : \n[1]PAIR\n[2]ODD\n')
    choose = int(input('You want be a pair or odd?\n').strip())

    if choose != 1 and choose != 2 :
        print('\033[1:31mIncorrect value!!\033[m')

    elif choose == 1 :
        time.sleep(1)
        print("I'm odd, let's go!")
        chance = int(input('Choose a number between 0 and 10 : \n'))
        result = machine + chance
        if result % 2 == 0 :
            print(f'\033[1:32mYou win!! Because I chosen {machine} and the result'
                  f' {result} is pair number!!\033[m')
            print('\033[1:36mWe go again!!\033[m\n')
            count += 1

        if result % 2 == 1 :
            print(f"\033[1:31mIm the winner because i chosen {machine} and the result is odd\033[m")
            break

    elif choose == 2 :
        time.sleep(1)
        print("I'm pair, let's go!")
        chance = int(input('Choose a number between 0 and 10 : \n'))
        result = machine + chance
        if result % 2 == 1 :
            print(f'\033[1:32mYou win!! Because I chosen {machine} and the result'
                  f' {result} is odd number!!\033[m')
            print('\033[1:36mWe go again!!\033[m\n')
            count += 1

        if result % 2 == 0 :
            print(f"\033[1:31mIm the winner because i chosen {machine} and the result is pair\033[m")
            break

print(f'You was winner \033[1:32m{count} times\033[m')
