# Q.1Write a Python program to print the following output
# output : \t hel\blo \t
# \’ python is easy \’
# \\ everyone should learn \\
# \n practice a lot \n
# --------------approach 1--------------------

# print("\\t hel\\blo \\t")
# print("\’ python is easy \’")
# print("\\\\ everyone should learn \\\\")
# print("\\n practice a lot \\n")

# --------------approach 2-------------------
# using raw string

# print(r"\t hel\blo \t")
# print(r"\’ python is easy \’")
# print(r"\\ everyone should learn \\")
# print(r"\n practice a lot \n")

# *********************************************************************************
# Q.2 Write a Python program to swap two numbers without using a third variable (use of an efficient algorithm is expected). Take the two numbers as an input from the user in one line only.

# --------------approach 1--------------------
# simple method

# a,b=map(int,input("Enter two numbers: ").split())
# print("a =",a,"\nb =",b)
# a,b=b,a
# print("\nSwapped numbers are:\na =",a,"\nb =",b)

# --------------approach 2-------------------
# using algorithm

# a,b=map(int,input("Enter two numbers: ").split())
# print("a =",a,"\nb =",b)
# a=a+b
# b=a-b
# a=a-b
# print("\nSwapped numbers are:\na =",a,"\nb =",b)

# *********************************************************************************
# Q.3 Write a Python program to determine if a year given as an input by the user is a leap year or not.

# --------------approach 1: simple approch--------------------
# year=int(input("Enter year: "))
# if year%4==0:
#     print("It is a leap year.")
# else:
#     print("It is not a leap year.")

# --------------approach 2: finest approch-------------------
# some complex algorithm, accurecy 100%
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# https://www.timeanddate.com/date/leapyear.html - article: why we not take leap year on every 4 years.This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.check in mobile

# def is_leap(year):
#     leap = ("It is not a leap year")

#     if (year%400==0):
#         leap=("It is a leap year")
#     elif (year%100 != 0 and year%4==0):
#         leap=("It is a leap year")


#     return leap

# year = int(input("Enter year: "))
# print(is_leap(year))

# *********************************************************************************
# Q.4 Write a Python program to print the table of any number n,taken as an input from the user.
# E.g. n=2
# 2*1 = 2
# 2*2 = 4
# .
# .
# .
# 2*10 = 20

# n=int(input("n="))
# for i in range(1,11):
#     print(f"{n}*{i} =",n*i)

# *********************************************************************************
# Q.5 Write a Python program to check whether the given number is prime or not. Take this number as an input from the user.

# --------------approach 1-------------------
# simple method 1
# n=int(input("Enter a number: "))

# if n<=1:
#     print(f"{n} is not prime.")
#     exit

# for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} is not prime.")
#             break
#         else:
#             print(f"{n} is prime.")
#             break

# --------------approach 2-------------------
# simple method 2

# n = int(input("Enter a number: "))
# # 1 is not prime
# if n == 1:
#     print(n, "is not Prime!!!")
# elif n > 1:
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break

#     if is_prime == True:
#         print(n, "is Prime!!!")
#     else:
#         print(n, "is not Prime!!!")
# else:
#     print("Enter a positive integer.")

# --------------approach 3-------------------
# simple and efficient way , don't know it works or not everytime

# n = int(input("Enter a number: "))
# if n<=1:
#     print(n, "is not Prime!!!")
# elif n==2 or n==3 or n==5 or n==7:
#     print(n, "is Prime!!!")
# elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
#     print(n, "is not Prime!!!")
# else:
#     print(n, "is Prime!!!")

# *********************************************************************************
# Q.6 Write a Python program to print following pattern
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# c=5
# for i in range(5,0,-1):
#     print(f"{c} "*i)
#     c-=1

# *********************************************************************************
# Q.7 Write a Python program to print GCD(greatest common divisor) of two numbers. Take these two numbers as an input from the user in a single line.

# --------------approach 1-------------------

# a,b=map(float,input("Enter two numbers: ").split())

# i = 1
# while(i <= a and i <= b):
#     if(a % i == 0 and b % i == 0):
#         gcd = i
#     i+=1

# print(f"\nGCD of {a} and {b} is {gcd}")

# --------------approach 2-------------------
# using function
# a,b=map(float,input("Enter two numbers: ").split())

# def gcd(x, y):
#     gcd = 1

#     if x % y == 0:
#         return y

#     for i in range(int(y / 2), 0, -1):
#         if x % i == 0 and y % i == 0:
#             gcd = i
#             break
#     return gcd

# print(f"\nGCD of {a} and {b} is {gcd(a, b)}")

# --------------approach 3-------------------
# using recursion

# a, b = map(float, input("Enter two numbers: ").split())

# def gcd(a, b):
#     if(b == 0):
#         return a
#     else:
#         return gcd(b, a % b)


# print(f"\nGCD of {a} and {b} is {gcd(a, b)}")

# --------------approach 4-------------------
# using temp variable

# a, b = map(float, input("Enter two numbers: ").split())
# num1=a
# num2=b

# while(b != 0):
#   temp = b
#   b = a % b
#   a = temp
# gcd = a

# print(f"\nGCD of {num1} and {num2} is {gcd}")

# *********************************************************************************
# Q.8 Write a Python program to remove the n th character from a string using function.

# def remove(s,c):
#     lst=[i for i in s]
#     del lst[c]
#     a="".join(lst)
#     print(a)

# string=input("Enter a string: ")
# n=int(input("Enter the index number of charecter which you want to remove: "))
# remove(string,n)

# *********************************************************************************
# Q.9 Write a Python program to print factorial of n using function. Take n as an input from the user.

# def fact(n):
#     factorial = 1
#     if n < 0:
#         print("Factorial of negative numbers does not exist.")
#     elif n == 0:
#         print("The factorial of 0 is 1")
#     else:
#         for i in range(1, n + 1):
#             factorial = factorial*i
#         print("The factorial of", n, "is", factorial)

# num = int(input("Enter a number: "))
# fact(num)

# *********************************************************************************
# Q.10 Write a Python program to print the length of a string without using the len() function(use a user defined function). Take this string as an input from the user.

# def length(string):
#     c=0
#     for i in string:
#         c+=1
#     print(f'Length of string "{string}" is {c}.\n')

# str1=input("Enter the string: ")
# length(str1)
