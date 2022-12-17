# Different types of list program
print("**"*50)

# Creating lists
num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Summary Table
print("\t\tSummary Table.\n")
print("The variable num_strings is a "+str(type(num_strings))+'.')
print("It contains the elements:"+str(num_strings)+'.')
print("The element " + str(num_strings[0]) +" is a " + str(type(num_strings[0])))

print("\nThe variable num_strings is a "+str(type(num_ints))+'.')
print("It contains the elements:"+str(num_ints)+'.')
print("The element " + str(num_ints[0])+" is a " + str(type(num_ints[0])))

print("\nThe variable num_strings is a "+str(type(num_floats))+'.')
print("It contains the elements:"+str(num_floats)+'.')
print("The element " + str(num_floats[0])+" is a " + str(type(num_floats[0])))

print("\nThe variable num_strings is a "+str(type(num_lists))+'.')
print("It contains the elements:"+str(num_lists)+'.')
print("The element " + str(num_lists[0])+" is a " + str(type(num_lists[0])))

# Sorting lists
print("\nNow sorting num_strings and num_ints...")
num_strings.sort()
print("Sorted num_strings:", str(num_strings))
num_ints.sort()
print("Sorted num_ints:", str(num_ints))

# conclusion after sorting num_strings and num_ints
print("\nStrings are sorted alphabetically while integers are sorted numerically!")

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)
