import time

program = True
menCount = 0
womanUnder20 = 0
age18 = 0
menList = []
womanList = []

while program :
    choose = str(input('You want continue to register a member?'
                       ' [\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()

    if choose == 'Y' :
        gender = str(input("What's the gender of him/her?"
                           " [\033[1:36mM\033[m]/[\033[1:31mF\033[m]\n")).strip().upper()
        name = str(input("What's the name of him/her?\n")).strip()
        age = int(input('How years old are him/her?\n'))

        if age > 18 :
            age18 += 1

        if gender == 'M' :
            menCount += 1
            menList.append(name)

        if gender == 'F' and age < 20 :
            womanUnder20 += 1
            womanList.append(name)

    if choose == 'N' :
        break

time.sleep(0.5)
print(f'After the end of registers...\n')
print(f'The quantity of \033[1:37mpersons\033[m over 18 is {age18} persons')
print(f'The quantity of \033[1:36mmens\033[m registered is {menCount} men')
print(f'The quantity of \033[1:31mwomans\033[m registered is {womanUnder20} women')
print(f'The name list of men is : {menList}')
print(f'The name list of women is : {womanList}')
