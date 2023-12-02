extensiveNumbers = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                  'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                  'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
program = True

while program :
    seeNumber = int(input('Write a number and see your extensive way :\n').strip())
    print(f'The number {seeNumber} in extensive version is \033[1:35m{extensiveNumbers[seeNumber]}\033[m')

    if seeNumber > 20 and seeNumber < 0 :
        seeNumber = int(input('Try again. Write a number between in 0 and 20 :\n'))

    choose = str(input('You want continue? [\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()

    if choose != 'N' and choose != 'Y' :
        print('Try again. Choose a correct value!')
        choose = str(input('You want continue? [\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()

    if choose == 'N' :
        break