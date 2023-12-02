import datetime
actualYear = datetime.datetime.now().year
yearsOfJob = 35
yearsOfRetirement = 0
person = {}

person['name'] = str(input("What's the functionary name?\n")).strip().title()
birth = int(input("What's your birth year?\n").strip())
person['jobRegister'] = int(input("What's your register number?(0 = have not)\n").strip())
person['age'] = actualYear - birth

if person['jobRegister'] == 0 :
    print('You do not have a job register...')

else :
    person['birthContract'] = int(input("What's your register year?\n").strip())
    person['grossSalary'] = float(input('How much is your gross salary?\n').strip())

    yearsLeft = actualYear - person['birthContract']
    retirement = yearsOfJob - yearsLeft

    yearsOfRetirement = person['age'] + retirement

print(f'The functionary is \033[1:36m{person["name"]}\033[m')

if person['jobRegister'] != 0 :
    print(f'Your gross salary is \033[1:32m{person["grossSalary"]}\033[m')
    print(f'Your age is {person["age"]} and left {yearsOfRetirement} years to retirement')
    print(f'Your register number is {person["jobRegister"]}')