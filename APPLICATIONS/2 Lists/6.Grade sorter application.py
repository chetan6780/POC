# Grade Sorter Application
print("**"*50)

# Welcome message.
print("Welcome To Grade Sorter Application.\n")

# create lists.
grades = []
grades.append(int(input("What is your first Grade (0-100):")))
grades.append(int(input("What is your second Grade (0-100):")))
grades.append(int(input("What is your third Grade (0-100):")))
grades.append(int(input("What is your forth Grade (0-100):")))

# Showing grades
print('\nYour grades are:', grades)
grades.sort(reverse=True)
print("Your grades form highest to lowest are", str(grades))

# removing lowest two grades
print("\nThe lowest grades will now be dropped.")
print("Removed grade: ", grades.pop(-1))
print("Removed grade: ", grades.pop(-1))

# Showing highest grade
print("\nYour remaining grades are : ", str(grades))
print("Nice work! Your highest grade is a "+str(grades[0])+'.')

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)
