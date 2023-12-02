program = True
wordsTuple = ()

while program :
    word = str(input('Write a word for add in word list :\n')).strip().upper()
    wordsTuple += (word,)

    choose = str(input('\nYou want continue? [\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()
    if choose == 'N' :
        break

for word in wordsTuple :
    print(f'\nThe word {word} have a vocal(s) : ', end='')
    for vocal in word :
        if vocal.upper() in 'AEIOU' :
            print(vocal, end=' ')

#outra maneira de fazer, adicionando uma nova tupla
'''
vocals = ('A','E','I','O','U')
searchedVocals = ()

print(f'The word {word} have the vocals :', end=' ')
for vocal in word :
    if vocal in vocals :
        searchedVocals += (vocal,)
        for times in range(0, 1) :
            print(f'{vocal}', end=' ')
'''