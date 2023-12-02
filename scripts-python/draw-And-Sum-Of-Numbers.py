import time
import random

numbersList = []
pairList = []

def randomNumbers() :
    for x in range(0, 5) :
        print('\033[1:36mGenerating random number...\033[m')
        time.sleep(1)
        randomNumber = random.randint(0, 100)
        print(randomNumber)
        numbersList.append(randomNumber)
    print(f"The values of numbers list is : ", end='')
    for value in numbersList :
        print(f'{value}', end='; ')
    print()
    print()

def pairSum() :
    for value in numbersList :
        if value % 2 == 0 :
            pairList.append(value)

    print(f"The numbers of pair list is : ", end='')
    for pair in pairList :
        print(f"{pair}", end='; ')
    print()
    print(f"The sum of pair numbers is {sum(pairList)}")

randomNumbers()
pairSum()
