#  Python Calculator Application
print("**"*50)

# Welcome message.
print("Welcome To Python Calculator Application.")

def add(a, b):
    sum_ = round(a+b, 4)
    print(f"\nThe sum of {a} and {b} is {sum_}.")
    return str(a) + " + " + str(b) + " = " + str(sum_)


def substract(a, b):
    sub = round(a-b, 4)
    print(f"\nThe difference of {a} and {b} is {sub}.")
    return str(a)+" - "+str(b)+" = "+str(sub)


def multiply(a, b):
    mul = round(a*b, 4)
    print(f"\nThe multiplication of {a} and {b} is {mul}.")
    return str(a)+" * "+str(b)+" = "+str(mul)


def divide(a, b=1):
    if b == 0:
        print("\nYou cannot divide by zero.")
        return "DIV ERROR"
    else:
        div = round(a/b, 4)
        print(f"\nThe division of {a} and {b} is {div}.")
        return str(a)+" / "+str(b)+" = "+str(div)


def exponent(a, b):
    expo = round(a**b, 4)
    print(f"The result of {a} raised to the {b} power is {expo}.")
    return str(a)+" ** "+str(b)+" = "+str(expo)


def main():
    history = []
    active = True
    while active:
        first_num, second_num = float(
            input("\nEnter a number: ")), float(input("Enter a number: "))
        option = input(
            "\nEnter an operation:\n-addition \n-subtraction \n-multiplication \n-division \n-exponentiation\n").strip().lower()
        if option.startswith("a"):
            history.append(add(first_num, second_num))
        elif option.startswith("s"):
            history.append(substract(first_num, second_num))
        elif option.startswith("m"):
            history.append(multiply(first_num, second_num))
        elif option.startswith("d"):
            history.append(divide(first_num, second_num))
        elif option.startswith("e"):
            history.append(exponent(first_num, second_num))
        else:
            print("Please enter a valid option.")
            history.append("OPP ERROR")

        # Continue or not
        Choice = input(
            "\nWould you like to run the program again (y/n): ").lower().strip()
        if Choice.startswith("y"):
            continue
        elif Choice.startswith("n"):
            active = False
            summury = ("Calculation Summary:")
            for action in history:
                print(action)
        else:
            summury = ("Calculation Summary:")
            for action in history:
                print(action)
            print("Please choose y/n only!")
            break


if __name__ == "__main__":
    main()

# End of programm.
print("\n\nThank you for using the Python Calculator Application. Goodbye.\n")
print("**"*50)
