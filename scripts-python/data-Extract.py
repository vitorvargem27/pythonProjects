numberList = []
program = True
numbersWrote = 0

while program :
    number = int(input('Write a number for add in the numbers list :\n').strip())
    numberList.append(number)
    numbersWrote += 1
    choose = str(input('You want continue? [\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()

    while choose != 'N' and choose != 'Y':
        print('Choose a right decision!')
        choose = str(input('You want continue? [\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()

        if choose == 'N' and choose == 'Y' :
            break

    if choose == 'N' :
        break

print(f'The quantity of numbers wrote is {numbersWrote}')

if 5 in numberList :
    print('\033[1:32mThe number 5 is on the number list!!\033[m')
else :
    print('\033[1:31mThe number 5 is not on the number list...\033[m')

numberList.sort(reverse=True)
print(f'The numbers list in reverse order is {numberList}')