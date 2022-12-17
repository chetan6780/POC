# This is a letter counter application.
print("**"*50)

# Welcome message.
print("\nWelcome to letter counter app \n")

name = input("What is your name:").title().strip()
print(f"\nHello {name}!")

# goal of app.
print('I will count number of times that a specific letter occurs in a message.\n')

message,world = input("Please Enter a message : ").lower(),input("\nWhich letter would you like to count the occurance of : ").lower()

letter_count = message.count(world)

# Result in f formating.
print(f"{name},your message has {letter_count} {world}'s in it.\n")

# End of programm.
print("Thank you for using this application!\n")
print("**"*50)
