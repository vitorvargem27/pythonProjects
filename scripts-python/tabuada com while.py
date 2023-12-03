import time
count = 0
number = 0
total = 0

while number >= 0 :
    number = int(input('Write a number for see your table :\n'))
    if number < 0 :
        break

    for count in range(0, 10):
        count += 1
        total = count * number
        time.sleep(1)
        print(f'{number} x {count} = {total}')

print('\033[1:31mEnd of program because you wrote a negative number \033[m')
