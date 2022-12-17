# Multiplication or Exponant table Application
print("**"*50)

# Welcome message.
print("Welcome To Multiplication or Exponant table Application.\n")

# Getting user input
name = input("What is your name:").title().strip()
num = float(input("What number would you like to work with:"))
message = name+",Math is cool!"

# Multipication table
print(f"Multiplication table for {num}\n")
for i in range(1, 11):
    mult = round((i*num), 2)
    print(f"\t{i}*{num} = {mult} ")

# Exponant table
print(f"\nExponant table for {num}\n")
for i in range(1, 11):
    Expo = round((i**num), 2)
    print(f"\t{i}*{num} = {Expo} ")

# Math is cool!
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)
