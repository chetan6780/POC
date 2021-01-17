import time

#  factor generator application
print("**"*50)

# Welcome message.
print("Welcome To factor generator application.")

active = True
while active:
    Choice = input("""\nEnter 1 or 2 from following:
1: Determine if a specific number is prime.
2: Determine all prime numbers within a set range.\n""")

    # Determine if a specific number is prime.
    if Choice == "1":
        num = int(input("\nEnter a number to determine if it is prime or not: "))
        # 1 is not prime
        if num==1:
            print(num, "is not Prime!!!")
        elif num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime == True:
                print(num, "is Prime!!!")
            else:
                print(num, "is not Prime!!!")
        else:
            print("Enter a positive integer.")

    # Determine all prime numbers within a set range.
    elif Choice == "2":
        lower_bound = int(input("\nEnter the lower bound of your range: "))
        upper_bound = int(input("Enter the upper bound of your range: "))
        print("Calculating.....")
        prime = []

        start_time = time.time()

        for num in range(lower_bound, upper_bound+1):
            # 1 is not prime
            if num > 1:
                is_prime = True
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
            else:
                is_prime = False

            if is_prime:
                prime.append(num)

        end_time = time.time()
        total_time = round(end_time-start_time, 8)

        print(f"\nCalculations took a total of {total_time} seconds.")
        print(f"\nFollowing are numbers between {lower_bound} to {upper_bound} which are prime ")

        # Print prime numbers
        continue_ = input("Press Enter to continue: ")
        for i in prime:
            print(i)

    else:
        print("Enter a valid choice!")

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
print("\n\nThank you for using the factor generator application. Goodbye.\n")
print("**"*50)
