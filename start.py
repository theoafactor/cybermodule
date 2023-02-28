import input_module

users = []
while True:
    users.append(input_module.user)
    print(users)
    if len(users) == 4:
        break