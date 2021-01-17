#  Shipping Accounts Program
print("**"*50)

# Welcome message.
print("Welcome To Shipping Accounts Program.\n")
users = ['Chetan', 'Chetan2', 'Chetan3', 'Chetan4', 'Chetan5']
Name = input("Hello, what is your username: ").strip().title()

# If user is registred.
if Name in users:
    print(f"\nHello {Name}. Welcome back to your account.\n")
    print("Current shipping prices are as follows:\n")
    print("Shipping orders 0 to 100: \t$5.10 each")
    print("Shipping orders 100 to 500: \t$5.00 each")
    print("Shipping orders 500 to 1000: \t$4.95 each")
    print("Shipping orders over 1000: \t$4.80 each\n")

    # Getting quantity
    quantiy = int(input("How many items would you like to ship: "))
    if quantiy < 100:
        price = 5.10
    elif quantiy < 500:
        price = 5.00
    elif quantiy <= 1000:
        price = 4.95
    elif quantiy > 1000:
        price = 4.80

    # Calculating bill
    bill = round((quantiy*price), 2)
    print(
        f"\nTo ship {quantiy} items it will cost you ${bill} at ${price} per item.")

    # Getting confirmation
    a = input("\nWould you like to place this order (Y/N): ").lower()
    t = True
    while t == True:
        if a.startswith("y"):
            print(f"Okay. Shipping your {quantiy} items.")
            t = False
            x = input("Press Enter to continue.....")
            print("Your order placed succesfully :-)")
        elif a.startswith("n"):
            print("Okay, no order is being placed at this time.")
            t = False
            x = input("Press Enter to continue.....")
            print("Your order is cancelled !!!")
        else:
            a = input("Please enter (Y/N): ").title()
            continue

# If user is not registred.
else:
    print("Sorry, you do not have an account with us.")

# End of programm.
print("\nThank you for using the Shipping Accounts Program. Goodbye.\n")
print("**"*50)
