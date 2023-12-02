import time

player = {}

totalGoals = 0
player['goals'] = []
player['name'] = str(input("What's the player name?\n")).title().strip()
player['timesPlayed'] = int(input(f'How much times are you played, {player["name"]}?\n').strip())

for times in range(0, player['timesPlayed']) :
    goals = int(input(f'How much goals {player["name"]} scored in the {times + 1}° match?\n').strip())
    player['goals'].append(goals)
    totalGoals += goals

for x in range(0, player['timesPlayed']) :
    print(f"The player {player['name']} are scored {player['goals'][x]} in the {x + 1}° match")

print('Calculating the sum of goals...')
time.sleep(1)
print(f"The total of goals is {totalGoals}")