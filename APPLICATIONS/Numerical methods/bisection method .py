# Redefine the values of a ,b and function

import math as m

def func(x):
    # return x**3 - x - 1
    # return x*x-3
    # return m.sin(x)-1/x
    # return x**2-m.sin(x)-0.5
    # return x*x*x-2*x-5
    # return x**3-20
    # return x**3 - 4*x + 9 
    return ((2.7182)**(-x))*(3.2*m.sin(x))-(0.5*m.cos(x))


def bisection(a, b):

    iterat = 0
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    while ((b-a) >= 0.0001):

        # Find middle point
        c = (a+b)/2

        # Check if middle point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
            print("b = c")
        else:
            a = c
            print("a = c")
        iterat += 1
        # print(func(2.5))
        print("itteration: ", iterat)
        print("function at a: ",func(a))
        print("function at b: ",func(b))
        print("function at c: ",func(c))
        print("value of function is :","%.4f" %func(c))
        print("The value of root is : ", "%.6f" % c)
        print()
    

    #     with open("Ans1.txt","a") as f:
    #         f.write(str(iterat)+"\n")
    #         f.write(str("%.4f" %func(c))+"\n")
    #         f.write(str("%.4f" % c)+"\n")
    #         f.write("\n")
    
    # with open("Ans1.txt","a") as f:
    #     f.write("=================================================================")


#1. Using bisection method find an appropriate root of equation sinx=1/x root lies between x=1 and x=1.5 carryout the computation upto 7th stage.

#2. find out the root of equation cosx=x*e^x by using bisection method correst upto 4 decimal places

#3. f(x)=x^2-sinx-0.5 for a,b=0,2 also epsilon=10^-3 (Relative error)

a = -100
b = 100
bisection(a, b)
