number = int(input('Write a number and see you factorial :\n').strip())


while number < 0 :
    print('\033[1:31mThe factorial is only for positive numbers!!')

if number >= 0 :
    factorial = 1
    multiplyNumber = 1

    while multiplyNumber <= number : #usa o multiply number e soma mais um a cada looping feito até chegar no numbero
        factorial *= multiplyNumber
        multiplyNumber += 1

    print(f'The result of {number}! is {factorial}')
