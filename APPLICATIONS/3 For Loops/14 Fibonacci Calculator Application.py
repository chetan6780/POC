# Fibonacci Calculator Applicationl̥
print("**"*50)

# Welcome message.
print("Welcome To Fibonacci Calculator Application.\n")

# Printing fibonacci numbers
num = int(
    input("How many digits of the Fibonacci Sequence would you like to compute: "))
fib = [1, 1]
print(f"The first {num} numbers of the Fibonacci sequence are:")
for i in range(0, num-2):
    x = fib[-1]+fib[-2]
    fib.append(x)

for a in fib:
    print(a)

# Golden Ratio values
print("\nThe corresponding Golden Ratio values are:")
for i in range(0, num):
    try:
        print(fib[i+1]/fib[i])
    except:
        pass

# Conclusion
print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618.....")

# End of programm.
print("\nThank you for using the Fibonacci Calculator Application.\n")
print("**"*50)

