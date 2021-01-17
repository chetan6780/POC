import math

# Quadratic 13: Factorial Calculator Application
print("**"*50)

# Welcome message.
print("Welcome To Factorial Calculator Application.\n")


num = int(input("What number would you like to compute the factorial of:"))

# Mathematical representation
print(str(num)+"! = ", end="")
for i in range(1, num):
    print(i, end="*")
print(num)

# Result from math library
print("\nHere is the result from the math library:")
fact_1 = math.factorial(num)
print(f"The factorial of {num} is {fact_1}\n")

# Result from my own algorithm
print("Here is the result from my own algorithm:")
fact_2 = 1
for i in range(1, num):
    fact_2 += fact_2*i
print(f"The factorial of {num} is {fact_2}\n")

# final result
if fact_1 == fact_2:
    print("It is shown twice that {0} = {1} !!!".format(
        num, fact_2))
else:
    print("Results are not identical ,please cheak your code again")

# End of programm.
print("\nThank you for using the Factorial Calculator Application. Goodbye.\n")
print("**"*50)
