sexualGender = str(input("What's your sexual gender?\n"))

while sexualGender != 'M' and sexualGender != 'F' :
    print('Informed sexual gender incorrect, try again!\n')
    sexualGender = str(input("What's your sexual gender?"))
print(f'Your sexual gender is {sexualGender}')
