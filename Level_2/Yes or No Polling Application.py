#  Yes or No Polling Application
print("**"*50)

# Welcome message.
print("Welcome To Yes or No Polling Application.\n")

# Getting inputs
issue = input(
    'What is the yes or no issue you will be voting on today: ').strip()
voters = int(
    input("What is the number of voters you will allow on the issue: "))
password = input("Set a password for polling results:").strip()

# Initializing variables
yes, no = 0, 0
results = {}

# Simulating voting
for i in range(voters):
    name = input("\nEnter your full name: ").strip().title()
    if name in results.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print(f"Here is our issue: {issue}.")
        vote = input("What do you think...yes or no: ").strip().title()
        if vote.startswith("Y"):
            yes += 1
            results[name] = "yes"
        elif vote.startswith("N"):
            no += 1
            results[name] = "no"
        else:
            results[name] = vote
        print(f"Thank you {name}! Your vote of {vote} has been recorded.")

# Number of people voted
total_votes = len(results.keys())
print(f"\nThe following {total_votes} people voted: ")
for i in results.keys():
    print("-\t",i)

# Isuue and result
print("\non the following issue:", issue)
if yes > no:
    print(f"Yes wins! {yes} votes to {no}.")
elif yes < no:
    print(f"Yes wins! {no} votes {yes} to .")
else:
    print(f"It was a tie! {yes} votes to {no}.")

# Getting full result
password0 = input(
    "\nTo see the voting results enter the admin password: ").strip()
if password0 == password:
    for key, value in results.items():
        print(f"Voter: {key} \t Vote: {value}")
else:
    print("Sorry, that is not the correct password. Goodbye...")

# End of programm.
print("\nThank you for using the Yes or No Polling Application. Goodbye.\n")
print("**"*50)
