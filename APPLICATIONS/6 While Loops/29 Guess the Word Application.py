import random

#  Guess the Word Application
print("**"*50)

# Welcome message.
print("Welcome To Guess the Word Application.")

game_dict = {"sports": ['basketball', 'baseball', 'soccer', 'football', 'tennis', 'curling'],
             "colors": ['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
             "fruits": ['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
             "classes": ['english', 'history', 'science', 'mathematics', 'art', 'health'],
             }

game_keys = [key for key in game_dict.keys()]  # List comprehension

# Main loop
active = True
while active:
    game_category = game_keys[random .randint(0, len(game_keys)-1)]
    game_word = game_dict[game_category][random.randint(0, len(game_category)-1)]

    blank_word = []
    for letter in game_word:
        blank_word.append("-")

    print(f"Guess a {len(blank_word)} letter word from the following category: {game_category}")

    # Convert list into string by using different methods
    """ 
        >>> Using .join method of strings
        print(" ".join(blank_word))

        >>> Using list comprehension
        blank_word = " ".join([str(element) for element in blank_word]) 

        >>> Using list comprehension with map function...>>>
            blank_word = " ".join(map(str, blank_word))
    """

    guess_count = 0
    guess = " "

    while guess != game_word:
        word="".join(map(str, blank_word))
        print(word)
        guess = input("\nEnter your guess: ").strip().lower()
        guess_count += 1

        # Guess is incorrect,continue
        if guess != game_word:
            print("That is not correct. Let us reveal a letter to help you!")
            on = True
            while on:
                letter_index = random.randint(0, len(blank_word)-1)
                if blank_word[letter_index] == "-":
                    blank_word[letter_index] = game_word[letter_index]
                    on = False

        # Guess is correst,break
        else:
            print(f"Correct! You guessed the word in {guess_count} guesses.")
            break

    # Continue or not
    Choice = input(
        "\nWould you like to run the program again (y/n): ").lower().strip()
    if Choice.startswith("y"):
        continue
    elif Choice.startswith("n"):
        active = False
    else:
        print("Please choose y/n only!")
        break

# End of programm.
print("\n\nThank you for using the Guess the Word Application. Goodbye.\n")
print("**"*50)
