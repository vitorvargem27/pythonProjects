sum = 0 #sempre iniciar uma variavel com 0 em caso de soma e usar ela na soma dentro do for

for x in range(0, 6) : #apenas abre o loop e o x não será utilizado
    number = int(input('Write a any number : \n'))
    if number % 2 == 0:
        sum += number #soma da variavel sum = 0 com os numeros colocados
print(sum)
