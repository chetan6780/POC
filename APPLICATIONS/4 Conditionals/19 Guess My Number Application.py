import random

#  Guess My Number Application
print("**"*50)

# Welcome message.
print("Welcome To Guess My Number Application.\n")

# Greeting
name = input("hello! What is your name:").strip().title()

# Random integer between 1 to 20.
print(f"Hello {name}! I am thinking of a number between 1 and 20.")
number = random.randint(1, 20)

# Guessing the number
for i in range(5):
    guess = int(input("Take a guess:"))

    if guess in range(1, 21):
        if guess > number:
            print("Your guess is too high")
        elif guess < number:
            print("Your guess is too low")
        else:
            guess_num = i+1
            print(
                f"Good job, {name}! You guessed my number in {guess_num} gusses.")
            if i == 4:
                print(f"Game over. The number i was thinking of was {number}.")
            break
    else:
        print("Enter a number between 1 to 20.")

# print("\nOhhh , you lost your 5 chances!! , Try again later.")


# End of programm.
print("\nThank you for using the Guess My Number Application. Goodbye.\n")
print("**"*50)
