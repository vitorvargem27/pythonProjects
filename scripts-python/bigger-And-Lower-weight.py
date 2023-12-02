weightList = []

for x in range(0, 5) :
    weight = float(input('Hou much is your weight?'))
    weightList.append(weight)
    weightList.sort() #deixa a lista em ordem crescente

print(f'The biggest weight is {weightList[0]} and the less weight is {weightList[4]}')
