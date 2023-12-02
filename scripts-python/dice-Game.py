import random
import time
import operator

'''allGamers = {}
ranking = []

for player in range(0, 4) :
    allGamers['name'] = str(input("What's your name?\n")).strip().title()
    allGamers['randomNumber'] = random.randint(1, 6)
    print('Generating your number...')
    time.sleep(1)
    print(f"{allGamers['name']}, your number is {allGamers['randomNumber']}")

ranking = sorted(allGamers.items(), key = operator.itemgetter(1), reverse=True)

print(ranking)'''

gamer = {}
allGamers = {}
numbers = []
biggestNumber = 0

for players in range(0, 4) :
    gamer['name'] = str(input("What's  the name of this time of play?\n"))
    gamer['number'] = random.randint(0, 6)
    numbers.append(gamer['number'])
    print('Choosing a random number for you...')
    time.sleep(1)
    print(f'You number is {gamer["number"]}\n')

    if gamer['number'] > biggestNumber :
        biggestNumber = gamer['number']

numbers.sort()

'''ranking = sorted(gamer.items(), key=operator.itemgetter(1), reverse=True) #itemgetter = gerar o item com indice 1'''

for player in allGamers :
    if biggestNumber == player['number'] :
        print(f'The winner is {player["name"]} with the number {player["number"]}')

for player in allGamers :
    for number in numbers :
        for x in range(3, 0) :
            if player['number'] == number :
                print(f"The {x}° player is {player['name']}")