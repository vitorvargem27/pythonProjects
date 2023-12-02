import datetime
adults = 0
noAdults = 0
year = datetime.date.today().year #ano atual puxado da biblioteca datetime

for quantityPeople in range(0, 7) :
    birth = int(input('What is your birth year?'))
    age = year - birth

    if age >= 18 :
        adults += 1
    else :
        noAdults += 1

print(f'The number of adults is {adults} and no adults is {noAdults}')
