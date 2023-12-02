number = int(input('Write a number for number table :\n'))

for x in range(0,10) :
    x += 1
    multiplication = x * number
    print(f'{number} x {x} = {multiplication}')

    for count in range(0, 10):
        count += 1
        total = count * number
        print(f'{number} x {count} = {total}')
