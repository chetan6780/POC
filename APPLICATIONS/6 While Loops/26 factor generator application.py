#  factor generator application
print("**"*50)

# Welcome message.
print("Welcome To factor generator application.\n")

active = True
while active:
    # Taking inputs
    num = int(input("\nEnter a number to determine all factors of that number: "))
    factors = []
    for i in range(1, num+11):
        if num % i == 0:
            factors.append(i)

    # Factors
    print(f"\nFactors of {num} are: ")
    for factor in factors:
        print("- ", factor)

    # Summary
    print("\nIn Summary: ")
    length = int(len(factors)/2)
    for i in range(length+1):
        print("- ", factors[i], "*", factors[-(i+1)], "=", num)

    # Continue or not
    Choice = input("\nRun again (y/n): ").lower().strip()
    if Choice.startswith("y"):
        continue
    elif Choice.startswith("n"):
        active = False
    else:
        print("Please choose y/n only!")
        break

# End of programm.
print("\n\nThank you for using the factor generator application. Goodbye.\n")
print("**"*50)
