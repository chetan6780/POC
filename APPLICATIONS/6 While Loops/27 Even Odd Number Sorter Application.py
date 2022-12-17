#  factor generator application
print("**"*50)

# Welcome message.
print("Welcome To Even Odd Number Sorter Application.")

non_nums = [' ', '.', '?', '!', '"', "'", ':', ';', '(', ')', '%', '$', '&', '#', '\n', "",
            '\t', '[', ']', '{', '}', '/', '\\', '-', '_', '+', '*', '|', '^', '<', '>', '',
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            ]

active = True
while active:
    # Taking inputs
    num_list = input(
        "\nEnter in a string of numbers separated by a comma (,) : ").strip()
    for non_num in non_nums:
        num_list = num_list.replace(non_num, '')
    num_list = num_list.split(",")

    # All even and odd numbers
    evens, odds = [], []
    print("\n---- Result Summary ----")
    for num in num_list:
        num = int(num)
        if num % 2 == 0:
            print(num, "is even!")
            evens.append(num)
        else:
            print(num, "is odd!")
            odds.append(num)

    # print even numbers
    enter = input(
        f"\nThe following {len(evens)} numbers are even, Press Enter to see:")
    evens.sort()
    for num in evens:
        print("-", num)

    # print odd numbers
    enter = input(
        f"\nThe following {len(odds)} numbers are odd, Press Enter to see:")
    odds.sort()
    for num in odds:
        print("-", num)

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
print("\n\nThank you for using the Even Odd Number Sorter Application. Goodbye.\n")
print("**"*50)
