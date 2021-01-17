import random

#  a game of Rock, Paper, Scissors
print("**"*50)

# Welcome message.
print("Welcome To a game of Rock, Paper, Scissors.\n")
rnd = int(input("How many rounds would you like to play: "))

# Defining variables ,create a list and a object to hold random intiger
moves = ['rock', 'paper', 'scissors']
p_score = 0
c_score = 0
num = random.randint(0, 2)

# start the game
for i in range(rnd):
    rnd_ = i+1
    print(f"""\nRound {rnd_}:
--------------------------------------------------------------
Player:{p_score} \t Computer:{c_score}
--------------------------------------------------------------""")
    inp = input(f"Time to pick...rock, paper, scissors: ").strip().lower()
    a = moves[num]
    print(f"\tComputer: {a}")
    print(f"\tplayer: {inp}")

    # If player type valid option
    if inp in moves:
        if inp == "rock" and a == "scissors":
            print("\tRock beats scissors!")
            p_score += 1
            print(f"\tYou win round {rnd_}.")

        elif inp == "scissors" and a == "rock":
            print("\tRock beats scissors!")
            c_score += 1
            print("\tComputer gets the point")

        elif inp == "scissors" and a == ("paper"):
            print("\tscissors cuts paper!")
            p_score += 1
            print(f"\tYou win round {rnd_}.")

        elif inp == "paper" and a == "scissors":
            print("\tscissors cuts paper!")
            c_score += 1
            print("\tComputer gets the point")

        elif inp == "paper" and a == "rock":
            print("\tPaper covers rock!")
            p_score += 1
            print(f"\tYou win round {rnd_}.")

        elif inp == "rock" and a == "paper":
            print("\tPaper covers rock!")
            c_score += 1
            print("\tComputer gets the point")

        elif inp == a:
            print("\tIt is a tie, how boring!")
            print("\tNo one gets the point.")

    # If player type valid option
    else:
        print("\tThat is not a valid game option!")
        c_score += 1
        print("\tComputer gets the point.")

# pritn the final result
if p_score > c_score:
    print("""\n--------------------------------------------------------------
You are the Winner!! :-)
--------------------------------------------------------------""")
elif p_score < c_score:
    print("""\n--------------------------------------------------------------
Winner: Computer :-(
--------------------------------------------------------------""")
else:
    print("""\n--------------------------------------------------------------
It's a Tie ,no one wins the game.
--------------------------------------------------------------""")

# End of programm.
print("\nThank you for using the a game of Rock, Paper, Scissors. Goodbye.\n")
print("**"*50)
