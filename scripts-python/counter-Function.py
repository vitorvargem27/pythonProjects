import time
program = True

def count(start, final, difference) :
    for x in range(start, final, difference) :
        print(f"{x}", end='; ', flush= True)
        time.sleep(0.5)
    print()

print('The counter of 1 to 10 is...')
count(1, 11, 1)
print('The counter of 10 to 0 is...')
count(10, -1, -2)

init = int(input('Write a number to start count : \n').strip())
finalNumber = int(input('Write a final number of the count :\n').strip())
sequence = int(input('Write a difference of the number in sequence :\n').strip())

if sequence == 0 :
    if finalNumber > init:
        count(init, finalNumber + 1, 1)

    if init > finalNumber:
        count(init, finalNumber - 1, -1)

else :
    if init > finalNumber:
        count(init, finalNumber - 1, -sequence)

    if finalNumber > init:
        count(init, finalNumber + 1, sequence)