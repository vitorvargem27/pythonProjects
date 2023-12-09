def studentsNotes() :
    studentsData["biggerNote"] = 0
    studentsData["lowerNote"] = 0
    studentsData["quantity"] = 0

    while program :
        name = str(input('Write a name os student :\n'))
        note = float(input("Write a note for the student :\n").strip())
        studentsData["situation"] = ''
        notesList.append(note)

        if studentsData["quantity"] == 0 :
            studentsData["biggerNote"] = note
            studentsData["lowerNote"] = note

        else :
            if note > studentsData["biggerNote"] :
                studentsData["biggerNote"] = note

            elif note < studentsData["lowerNote"] :
                studentsData["lowerNote"] = note

        studentsData["quantity"] += 1
        choose = str(input('You want continue?[\033[1:32mY\033[m]/[\033[1:31mN\033[m]\n')).strip().upper()

        if choose != 'N' and choose != 'Y' :
            print('\033[1:31mInvalid choose!!\033[m')

        else :
            if choose == 'N' :
                break

    average = sum(notesList) / studentsData["quantity"]
    studentsData["average"] = round(average, 2)

    addSituationOnList = str(input('Are you want add the situation on your all data?\n')).strip().upper()

    while addSituationOnList != 'N' and addSituationOnList != 'Y':
        print('\033[1:31mWrite a valid choose!!\033[m')
        addSituationOnList = str(input('Are you want add the situation on your all data?\n')).strip().upper()

    else:
        if addSituationOnList == 'Y':
            if studentsData["average"] > 5:
                studentsData["situation"] = 'Approved Class'

            else:
                studentsData["situation"] = 'Reproved Class'

        elif addSituationOnList == 'N':
            studentsData["situation"] = 'Was not informed'

    print()

    for key, value in studentsData.items() :
        valueConference = isinstance(value, (str))

        if valueConference == True :
            if value == 'Approved Class' :
                print(f"{key} : \033[1:32m{value}\033[m")

            else :
                print(f"{key} : \033[1:31m{value}\033[m")

        else :
            if key == 'quantity' :
                print(f"{key} : \033[1:36m{value:.0f}\033[m")

            elif value > 5 :
                print(f"{key} : \033[1:32m{value:.2f}\033[m")

            else :
                print(f"{key} : \033[1:31m{value:.2f}\033[m")

program = True
sumAllNotes = 0
notesList = []
studentsData = {}
average = 0

studentsNotes()