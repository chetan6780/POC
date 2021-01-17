import cmath

# Quadratic Equation Solver Application
print("**"*50)

# Welcome message.
print("Welcome To Quadratic Equation Solver Application.\n")

# description of a quadratic equation and complex numbers
print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.\n\n")

# Getting number of equations to be solved
eqations = int(input("How many equations would you like to solve today: "))

# Solutin of quadratic eqations
for i in range(1, eqations+1):
    print(f"\nSolving equation #{i}")
    print("---------------------------------------------------------------")
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    print(f"\nThe solutions to {a}x^2 + {b}x + {c} = 0 are:")
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}\n")

# End of programm.
print("\nThank you for using the Quadratic Equation Solver App. Goodbye.\n")
print("**"*50)
