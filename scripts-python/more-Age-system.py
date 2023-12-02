maisVelho = ''
maiorIdade = 0
mulheresMenos20 = 0
soma = 0


for x in range(4):
    nome = str(input('Qual o seu nome?\n')).title().strip()
    idade = int(input('Quantos anos você tem?\n'))
    sexo = str(input('Sexo : (F/M)\n')).upper().strip()

    if sexo != 'F' and sexo != 'M':
        print('Digite um gênero válido na próxima')

    elif idade < 0 :
        print('Digite uma idade correta!')

    else :

        if idade > maiorIdade: # se a idade digita for maior que a que já está lá, substituir
            maisVelho = nome #também substitui o nome
            maiorIdade = idade #substitui a maior idade de todos

        if sexo.upper() == 'F' and idade < 20 :
            mulheresMenos20 += 1 #soma uma mulher a cada mulher menor de 20 anos

    soma += idade #soma cada idade a cada looping feito

mediaIdades = soma / 4

print(f'O nome do mais velho é {maisVelho}\n'
      f'O número de mulheres com menos de 20 é {mulheresMenos20}\n'
      f'E a média das idades é {mediaIdades}')
