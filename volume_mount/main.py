username = input("enter your username or press enter to proceed.")

if username:
    with open('user_info.txt', 'a') as file:
        file.write(username + "\n" )

show_info = input("Do you want to see all names ? y/n")

if show_info == 'y':
    try:
        with open('user_info.txt' , 'r') as file:
            content = file.readlines()

    except Exception as e:
        print(e,type(e))

    else:
        for line in content:
            print(f"{line.rstrip()}")
