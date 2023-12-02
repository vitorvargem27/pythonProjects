sum = 0
count = 0
for number in range(1, 500 + 1, 2) :

    if number % 3 == 0 :
        count += 1 #soma mais um a cada multiplo de 3 encontrado
        sum += number #soma o number/numero multiplo ao que já tem na soma

    print(sum)
