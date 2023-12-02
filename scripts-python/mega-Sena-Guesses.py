program = True

studentList = []
allStudentsList = []
alumnsCount = 0

while program :
    name = str(input("What's the name of the student?\n")).strip().title()
    firstNote = float(input('How much is the first note of him/her?\n').strip())
    secondNote = float(input('How much is the second note of him/her?\n').strip())

    average = (firstNote + secondNote) / 2

    studentList.append(name)
    studentList.append(firstNote)
    studentList.append(secondNote)
    studentList.append(average)

    allStudentsList.append(studentList[:])
    studentList.clear()
    alumnsCount += 1

    choose = str(input('You want continue?\n')).strip().upper()

    while choose != 'N' and choose != 'Y' :
        choose = str(input('You want continue?\n')).strip().upper()

    if choose == 'N' :
        break

for x in range(0, alumnsCount) :
    print(f'The data of the {x + 1}° student is :')
    print(f'Name : {allStudentsList[x][0]}')

    if allStudentsList[x][-1] > 5 :
        print(f'Average : \033[1:32m{allStudentsList[x][-1]}\033[m')

    else : print(f'Average : \033[1:31m{allStudentsList[x][-1]}\033[m')

noteConsult = True

while noteConsult :
    student = int(input("What's the student are you want consult?(in number)(999 break)").strip())

    print(f'Name{allStudentsList[student][0]:.>32}')
    print(f'Average{allStudentsList[student][-1]:.>28}')
    
    if student == 999 :
        break
