import random

# Defining the class Creature


class Creature():
    """Creating a creature"""

    def __init__(self, name):
        """Initializing attributes"""
        self.name = name.title()
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 2

        self.is_sleeping = False
        self.is_alive = True

    def eat(self):
        """Creatuer will eat a meal"""
        # make sure there is food available
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1, 4)
            print(f"{self.name} ate a great meal.")
        else:
            print(f"{self.name} doesn't have any food! Better forage for some.")

        # If the hunger is less than zero, set it to zero
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        """Creature wants to play"""
        num = random.randint(1, 2)
        print(f"\n{self.name} wants to play game.")
        print(self.name, "is thinking of a number 0, 1, or 2.")
        guess = int(input('whats your guess: '))
        if guess == num:
            print("You are absolutely Right!!!")
            self.boredom -= 3
        else:
            print(
                f"Sorry but the guess is incorrect,{self.name} was thinking about {num}.")
            self.boredom -= 1

        # If the boredom is less than zero, set it to zero
        if self.boredom < 0:
            self.boredom = 1

    def sleep(self):
        """Creature is sleeping"""
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        print(self.name, "is sleeping....zzzz.....zzzzz...zzzz")

        # If tiredness or boredom is less than zero, set it to zero
        if self.tiredness < 0:
            self.tiredness = 1

        if self.boredom < 0:
            self.boredom = 1

    def awake(self):
        """Creature is awake or not"""
        num = random.randint(0, 1)

        # If creature wakes up, set tiredness to zero!
        if num == 0:
            print(self.name, "just woke up.")
            self.is_sleeping = False
            self.boredom = 0
        else:
            print(self.name, "won't woke up.")
            self.sleep()

    def clean(self):
        """Creature took the bath"""
        self.dirtiness = 0
        print(f"{self.name} just took a bath.All clean!")

    def forage(self):
        """Simulate foraging for food. This will increase the creatures food attribute however, it will also increase their dirtiness"""
        food_found = random.randint(0, 4)
        self.food += food_found
        self.dirtiness += 2
        print(f"{self.name} found {food_found} pieces of food!")

    def show_values(self):
        """Display all information of creature"""
        print(f"\nCreature Name:{self.name}")
        print(f"Hunger (0-10): {self.hunger}")
        print(f"Borebom (0-10): {self. boredom}")
        print(f"Tiredness (0-10): {self.tiredness}")
        print(f"Dirtiness (0-10): {self.dirtiness}")

        print(f"\nFood inventory : {self.food} pieces")

        # Show current sleeping status
        if self.is_sleeping:
            print("Current Status: Sleeping")
        else:
            print("Current Status: Awake")

    def increment_values(self, difficulty):
        """User must set an arbitrary difficulty. This will control how much "damage" you take each round. Update the current values of the creature based on this difficulty."""

        self.hunger += random.randint(0, difficulty)

        # If the creature is awake, he should be growing tired and growing bored.
        if self.is_sleeping == False:
            self.boredom += random.randint(0, difficulty)
            self.tiredness += random.randint(0, difficulty)

        self.dirtiness += random.randint(0, difficulty)

    def kill(self):
        """Kill the creature or not"""
        if self.hunger >= 10:
            print(f"{self.name} starved to death.")
            self.is_alive = False

        elif self.dirtiness >= 10:
            print(f"{self.name} suffered an infection and died.")
            self.is_alive = False

        elif self.boredom >= 10:
            self.boredom = 0
            print(f"{self.name} is bored and falling asleep.")
            self.is_sleeping = True

        elif self.tiredness >= 10:
            self.tiredness = 10
            print(f"{self.name} is tierd and fallind asleep.")
            self.is_sleeping = True


# Defining the functions.

def show_menu(Creature):
    if Creature.is_sleeping:
        choice = input("\nEnter '6' to try and wake up: ")
        choice = '6'
    else:
        print("\nEnter '1' to eat.")
        print("Enter '2' to play.")
        print("Enter '3' to sleep.")
        print("Enter '4' to take a bath.")
        print("Enter '5' to forage for food.")
        choice = input("\nWhat is your choice: ")

    return choice


def call_action(Creature, choice):
    """Depending upon choice call the appropriate class method."""
    if choice == '1':
        Creature.eat()
    elif choice == '2':
        Creature.play()
    elif choice == '3':
        Creature.sleep()
    elif choice == '4':
        Creature.clean()
    elif choice == '5':
        Creature.forage()
    elif choice == '6':
        Creature.awake()
    else:
        print("Sorry, that is not a valid move.")


def main():

    #  Pythonagachi(pet) Simulator Applicaton
    print("**"*50)

    # Welcome message.
    print("Welcome To Pythonagachi(pet) Simulator Applicaton.")

    # Main code -choose difficuty level
    active = True
    while active:
        diff = int(input("\nPlease choose the difficulty level (1-5): "))
        if diff > 5:
            diff = 5
        elif diff < 1:
            diff = 1
        name = input(
            "What name would you like to give your pet Pythonagachi(pet): ")

        # creating Creature object
        plyr = Creature(name)
        rounds = 1

        # if creature is alive run this code
        while plyr.is_alive:
            print("-"*100)
            print("# Round:", rounds)

            plyr.show_values()
            choice = show_menu(plyr)  # returns the choice
            call_action(plyr, choice)

            print(f"\n-----# Round {rounds} summury:----")
            plyr.show_values()

            input("\nPress Enter to continue....")
            plyr.increment_values(diff)
            plyr.kill()
            rounds += 1

        print("\n-----R.I.P.-----")
        print(f"{plyr.name} survived a total {rounds}.")

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
        print("\n\nThank you for using the Pythonagachi(pet) Simulator  Applicaton. Goodbye.\n")
        print("**"*50)


if __name__ == "__main__":
    main()


