sum = 0
totalNumbers = 0
number = int(input('Write a any numbers...[The number 999 end the program]\n').strip())

while number < 999 :
    sum += number
    totalNumbers += 1
    number = int(input('Write a any numbers...[The number 999 end the program]\n').strip())

print(f'Wrote {totalNumbers} numbers and the sum is {sum}')
