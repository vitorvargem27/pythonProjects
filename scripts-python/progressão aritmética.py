firstNumber = int(input('Write a first number of sequency : \n'))
difference = int(input('Write a difference between this numbers : \n'))
decimoTermo = firstNumber + (10 - 1) * difference
sequence = [] #construindo um array de números da PA

for x in range(firstNumber, decimoTermo + 1, difference) :
    sequence.append(firstNumber) #append usado para adicionar um item para a PA
    firstNumber += difference

print(sequence)
