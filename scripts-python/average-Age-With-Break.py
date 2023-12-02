times = 0
total = 0
listNumbers = []
answer = str(input("Let's start the program?[\033[1:32mY\033[m/\033[1:31mN\033[m]")).upper()

while answer != 'N' and answer != 'Y' :
    print('\033[1:31mWrite a correct answer!!\033[m\n')
    answer = str(input('You want continue?[\033[1:32mY\033[m/\033[1:31mN\033[m]')).upper()

while answer == 'Y' :
    number = int(input('Write a numbers and see the magic...\n'))
    listNumbers.append(number)
    total += number
    times += 1
    answer = str(input('You want continue?[\033[1:32mY\033[m/\033[1:31mN\033[m]')).upper()
    while answer != 'N' and answer != 'Y':
        print('\033[1:31mWrite a correct answer!!\033[m')
        answer = str(input('You want continue?[\033[1:32mY\033[m/\033[1:31mN\033[m]')).upper()

average = total / times
listNumbers.sort()
print(f'The average of this numbers is \033[1:32m{average:.2f}\033[m')
print(f'The lower number is {listNumbers[0]} and the biggest is {listNumbers[-1]}')
