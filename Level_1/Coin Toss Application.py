import random

#  Coin Toss Application
print("**"*50)

# Welcome message.
print("Welcome To Coin Toss Application.\n")

# Get input
print("I will flip a coin a set number of times.")
f_count = int(input("How many times would you like me to flip the coin: "))
p_result = input(
    "Would you like to see the result of each flip (y/n): ").strip().lower()

# Defining variables
heads = 0
tails = 0

# Flipping the coin
print("\nFlipping !!!\n")
for i in range(f_count):
    num = random.randint(0, 1)
    if num == 1:
        heads += 1
        if p_result.startswith("y"):
            print("HEADS")
    else:
        tails += 1
        if p_result.startswith("y"):
            print("TAILS")
    flip_num = i+1
    if heads == tails:
        print(
            f"At {flip_num} flips, the number of heads and tails were equal at {heads} each.")

# Calculating percentages
percent_h = round(((heads/f_count)*100), 4)
percent_t = round(((tails/f_count)*100), 4)

# Printing result
print(f"\nResults Of Flipping A Coin {f_count} Times:\n")
if f_count >= 500:
    print("Side \t\tCount \t\t\tPercentage")
elif f_count > 200000:
    print("Side \t\tCount \t\t\t\tPercentage")
else:
    print("Side \t\tCount \t\tPercentage")
print("Heads\t\t", f"{heads}/{f_count}\t\t", percent_h)
print("Tails\t\t", f"{tails}/{f_count}\t\t", percent_t)

# End of programm.
print("\nThank you for using the Coin Toss Application. Goodbye.\n")
print("**"*50)
