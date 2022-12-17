
# Binary Hexadecimal Conversion Application
print("**"*50)

# Welcome message.
print("Welcome To Binary Hexadecimal Conversion Application.\n")

num=int(input("Compute binary and hexadecimal values up to the following decimal number:"))
print("\nGenerating lists....complete!")
print("\nUsing slices, we will now show a portion of each list.")
start_num=int(input("What decimal number would you like to start at:"))
end_num= int(input("What decimal number would you like to stop at:"))

print(f"\nDecimal values from {start_num} to {end_num}:")
for i in range(start_num,end_num+1):
    print(i)

print(f"\nBinary values from {start_num} to {end_num}:")
for i in range(start_num,end_num+1):
    print(bin(i))

print(f"\nHexadecimal values from {start_num} to {end_num}:")
for i in range(start_num,end_num+1):
    print(hex(i))

print(f"\nPress Enter to see all values from 1 to {num}.")
a=input()
print("Decimal----Binary----Hexadecimal")
print("----------------------------------------------------------")
for i in range(1,num):
    print(str(i)+"----"+str(bin(i))+"----"+str(hex(i)))

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)



"""
#Alternative given

print("Welcome to the Binary/Hexadecimal Converter App")

# Get user input and generate lists.
max_value = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_value+1))
binary = []
hexadecimal = []
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating lists...Complete!")

# Get slicing index from user.
print("\nUsing slices, we will now show a portion of each list.")
lower_range = int(input("What decimal number would you like to start at: "))
upper_range = int(input("What decimal number would you like to stop at: "))

# Slice through each list individually
print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) +":")
for num in decimal[lower_range-1:upper_range]:
    print(num)

print("\nBinary values from " + str(lower_range) + " to " + str(upper_range) +":")
for num in binary[lower_range-1:upper_range]:
    print(num)

print("\nHexadecimal values from " + str(lower_range) + " to " + str(upper_range)+ ":")
for num in hexadecimal[lower_range-1:upper_range]:
    print(num)

# Output the whole list to the screen
input("\nPress Enter to see all values from 1 to " + str(max_value) + ".")
print("Decimal----Binary----Hexadecimal")
print("----------------------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "----" + str(b) + "----" + str(h))
"""