def verifyUser(userTest) :
    code = 0
    while program :
        userTest["name"] = str(input('Write a username to add in users list:\n')).strip()
        userTest["code"] = code

        if len(usersName) == 0 :
            usersName.append(userTest["name"])
            allUsers.append(userTest.copy())
            codeList.append(code)
            code += 1
            print(codeList)
            
        elif len(usersName) > 0 :
            for x in range(0, len(usersName)) :
                while userTest["name"] == usersName[x] :
                    print(f"\033[1:31mThe name {userTest["name"]} is already existent!!\033[m")
                    userTest["name"] = str(input('Write a username to add in users list:\n')).strip()

                    if userTest["name"] != usersName[x] :
                        break

            usersName.append(userTest["name"])
            allUsers.append(userTest.copy())
            codeList.append(code)
            code += 1
            print(usersName)

        choose = str(input('You want continue on the register program?')).strip().upper()

        while choose != 'N' and choose != "Y" :
            print('\033[1:31mYou wrote a incorrect value\033[m')
            choose = str(input('You want continue on the register program?')).strip().upper()

        if choose == 'N' :
            break

    for i in range(0, len(allUsers)) :
        print(f"User register : {allUsers[i]}")

program = True
counter = 0
user = {}
allUsers = []
usersName = []
codeList = []

verifyUser(user)