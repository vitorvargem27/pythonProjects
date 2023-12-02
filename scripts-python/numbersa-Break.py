sum = 0
times = 0
number = 0

while True :
    number = int(input('Write a any number for see the sum of all them : (999 is the break number)\n'))
    if number == 999 :
        break
    sum += number
    times += 1


print(f'The sum of {times} numbers is {sum}')
