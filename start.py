from input_module import getUserData

users = []

print("Enter 'Y' for Yes or 'N' for No")
mode_option = input("Enter the app mode: " )

while True:
    user = getUserData(mode_option)

    if user == None:
        print("This app is not active")
        break
    else:
        users.append(user)
        print('Current users: ' + str(users))
        if len(users) == 2:
            break
    

print(users)

    
