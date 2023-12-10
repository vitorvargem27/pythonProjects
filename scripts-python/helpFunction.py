def interativeHelp(analysisParameter) :
    print(f"\033[1:46m{analysisParameter:>10}" + (' ' * 5) + '\033[m')
    print("\033[1:44m~\033[m" * 33)
    print(f"\033[1:36:44m{analysisParameter:>10} command access!! " + (' ' * 5) + "\033[m")
    print("\033[1:44m~\033[m" * 33)
    help(analysisParameter)

program = True
while program :
    functionParameter = str(input('\033[1:36:42mWhat function are you want analise?\033[m\n')).strip().lower()
    interativeHelp(functionParameter)

    if functionParameter == 'fim' :
        break