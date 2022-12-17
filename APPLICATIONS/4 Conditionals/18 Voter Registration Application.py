#  Voter Registration Application
print("**"*50)

# Welcome message.
print("Welcome To Voter Registration Application.\n")

# ● Get user input for their name and ege
name = input("Please enter your name:").strip().title()
age = int(input("Please enter your age:").strip())

politicalParties = ["BJP", "NCP", "SHIVSENA", "MANASE", "BJD", "INDIPENDENT"]

# Check the elegibility.if elegible
if age > 17:
    print(
        f"\nCongratultions {name}! You are old enough to register to vote.\n")
    print("Here is a list of political parties to join:")
    for party in politicalParties:
        print("-", party)

    # Joining a party
    p_join = input("\nWhat party would you like to join:").strip().upper()

    if p_join in politicalParties:
        print(f"\nCongratulations {name}! You have joined the {p_join} party!")

    if p_join == "BJP" or p_join == "SHIVSENA":
        print("That is a major party!")
    elif p_join == "INDIPENDENT":
        print("You are an independent person!")

# Not eligible
else:
    print("You are not old enough to register to vote.")

# End of programm.
print("\nThank you for using the Voter Registration Application. Goodbye.\n")
print("**"*50)
