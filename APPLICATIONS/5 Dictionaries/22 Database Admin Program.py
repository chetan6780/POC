#  Database Admin Program
print("**"*50)

# Welcome message.
print("Welcome To Database Admin Program.\n")

# Create a dictionary
log_on_information = {"admin00": "12345678",
                      "ch1": "a2345678",
                      "ch2": "b2345678",
                      "ch3": "c2345678",
                      "ch4": "d2345678", }

# Get username
username = input("Enter your username: ").strip().lower()

# Getting password
if username in log_on_information:
    password = input("Enter your password: ")
    # if password correct
    if password == str(log_on_information[username]):
        print(f'\nHello {username}! You are logged in!')
        if username == "admin00":
            print("\nHere is the current user database: ")
            for key, value in log_on_information.items():
                print('Username:', key, '\t\tPassword:', value)
        else:
            # if user want to change password.
            change_password = input("Would you like to change your password: ").strip().lower()
            if change_password == "yes":
                print("\nNew password must be 8 characters long.")

                # asking new password
                t = True
                while t == True:
                    new_password = input("What would you like your new password to be (min 8 chars): ")
                    if len(new_password) >= 8:

                        # cheack if passwprd is same as old
                        t = True
                        while t == True:
                            if password == new_password:
                                print(
                                    "\nNew password cannot be same as old password.")
                                break
                            else:
                                print(
                                    f"{username} your new password is {new_password}")
                                log_on_information[username] = new_password
                                t = False
                    else:
                        print("\nNew password must be 8 characters long!")
            else:
                pass
    else:
        print('Incorrect Password!')
else:
    print('Username not in database, goodbye.')

# End of programm.
print("\nThank you for using the Database Admin Program. Goodbye.\n")
print("**"*50)
