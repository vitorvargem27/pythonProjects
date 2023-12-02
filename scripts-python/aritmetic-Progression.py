pa = []
numbers = 0

firstNumber = int(input('Write a first number of the sequence : \n'))
difference = float(input('Write the difference between the numbers of the sequence\n'))

number = firstNumber
tenTerm = firstNumber + (10 - 1) * difference

while number <= tenTerm :
    pa.append(number)
    number += difference

print(pa)
print('STOP')

termRandom = int(input('How much terms you need see more?').strip())
term = firstNumber + (termRandom - 1) * difference

count = 1
while termRandom != 0 :
    while count <= 10 :
        pa.append(number)
        number += difference
        count += 1
        print(pa)

print('\033[1:31mEnd of the program...')

