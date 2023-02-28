# Collect data (username and password) from users
""" 
    Collects data from users. The data will be username and password
"""
def getUserData(mode):

    if mode == "Y":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = {
            "username": username,
            "password": password
        }

        return user

    else:
        return None



