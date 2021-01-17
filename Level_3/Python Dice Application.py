import random

#  Python Dice Application
print("**"*50)

# Welcome message.
print("Welcome To Python Dice Application.")


def dice_sides():
    sides = int(input("\nHow many sides would you like on your dice: "))
    return sides


def dice_number():
    num = int(input("How many dice would you like to roll: "))
    return num


def roll_dice(sides=6, num=1):
    dice = []
    print(f"You rolled {num} dice with {sides} sides")
    print("\n-----Results are as followed-----")

    for i in range(num):
        value = random.randint(1, sides)
        print("\t", value)
        dice.append(value)

    return dice


def sum_dice(dice):
    print(f"The total value of your roll is {sum(dice)}.")


def roll_again():
    again = input("\nWould you like to roll again (y/n): ").strip().lower()
    if again.startswith("y"):
        roll = True
    else:
        roll = False
    return roll


def main():
    roll = True
    while roll:
        d_sides = dice_sides()
        d_number = dice_number()

        roll_d = roll_dice(d_sides, d_number)

        sum_dice(roll_d)
        roll_again()


if __name__ == "__main__":
    main()

# End of programm.
print("\n\nThank you for using the Python Dice Application. Goodbye.\n")
print("**"*50)
