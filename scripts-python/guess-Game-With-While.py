import random

randomNumber = random.randint(0, 10)
print('\033[1:36mLet is go to the try hit my number?\033[m\n')
answer = int(input("What's the number between 0 and 10 you want try?\n"))
tryTimes = 0

while answer != randomNumber :
    print('\033[1:31mOh no, write a number again!!\033[m')
    answer = int(input("What's the number of you want try?\n"))
    tryTimes += 1

print(f'\033[1:32mYes!! My number is {randomNumber}, and you needed {tryTimes} times for this correct answer\033[m')
