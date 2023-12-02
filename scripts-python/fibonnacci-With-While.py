firstTerm = 0
secondTerm = 1
count = 1

termsChoosed = int(input('How much terms you need see in the Fibonacci Sequency?\n'))

while count <= termsChoosed :
    nextTerm = firstTerm
    print(nextTerm)
    nextTerm = firstTerm + secondTerm
    firstTerm = secondTerm # o antigo segundo vira primeiro para somar com o proximo termo
    secondTerm = nextTerm # o proximo vira o segundo para somar para o proximo termo
    count += 1
