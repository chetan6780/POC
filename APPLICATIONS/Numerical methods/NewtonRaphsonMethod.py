import math as m

def func(x):
    # return x * x * x - x * x + 2
    # return (((m.e)**-x)*(3.2*m.sin(x))-0.5*m.cos(x))
    return x**2-4*x+4

def derivFunc(x):
    return 3 * x * x 

# Function to find the root
def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
        print("The value of the root is : ", "%.6f" % x)


    print("\nThe value of the root is : ", "%.4f" % x)


# Driver program to test above
x0 = 1  # Initial values assumed
newtonRaphson(x0)
