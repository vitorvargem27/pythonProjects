for x in range(0, 10):
    phrase = str(input('\nEscreva uma frase para ver se ela é palíndroma : \n')).strip().upper()

    junta = phrase.replace(' ', '')
    contrario = junta[::-1] #o [::-1] serve para ver no sentido contrário da coisa
    print(junta)
    print(contrario)

    if junta == contrario :
        print(f'A palavra {phrase.lower()} é polindroma')

    else:
        print(f'A palavra {phrase.lower()} não é polindroma')
