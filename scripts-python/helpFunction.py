def interativeHelp() :
    program = True
    while program :
        functionParameter = str(input('\033[1:36:42mWhat function are you want analise?\033[m\n')).strip().lower()
        print(f"\033[1:46m{functionParameter:>10}" + (' ' * 5) + '\033[m')
        print("\033[1:44m~\033[m" * 33)
        print(f"\033[1:36:44m{functionParameter:>10} command access!! " + (' ' * 5) + "\033[m")
        print("\033[1:44m~\033[m" * 33)
        help(functionParameter)

        if functionParameter == 'fim' :
            print('FIM DE JOGO')
            break


interativeHelp()