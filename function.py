def getUsername(mode):
    if mode == True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        return {
            "username": username,
            "password": password
        }
    else:
        return None
   



# call the function
feedback = getUsername(False) #argument

if feedback is None:
    print("This app has been disabled")
else:
    print("This is "+ str(feedback))