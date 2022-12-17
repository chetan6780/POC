# Quadratic Equation Solver Application
print("**"*50)

# Welcome message.
print("Welcome To Grade Point Average Calculator Application.\n")

# Original grades
name = input("What is your name: ").title()
sub = int(input("How many grades would you like to enter: "))
grades = []

for i in range(sub):
    grades.append(float(input("Enter grade: ")))
print("\nGrades Highest to Lowest:")
grades_original = grades.copy()
grades.sort(reverse=True)

for grade in grades:
    print(grade)
print("\n{0}'s Grade Summary:\n ".format(name))
print("Total Number of Grades:", len(grades))
print("Highest Grade:", grades[0])
print("Lowest Grade:", grades[-1])
average_1 = round(sum(grades)/len(grades), 2)
print("Average:", average_1)

# Desired grades
desired_avg = float(input("\nWhat is your desired average: "))
print(f"\nGood luck {name}!")
grade_req = round(desired_avg*(len(grades)+1) - sum(grades), 2)  # 79*(5+1)-sum
print("You will need to get a {0} on your next assignment to earn a {1} average.".format(
    grade_req, desired_avg))

print("\nLets see what your average could have been if you did better/worse on an assignment.")
grade_change = float(input("\nWhat grade would you like to change: "))
grades.remove(grade_change)
grade_changed = float(
    input(f"What grade would you like to change {grade_change} to:"))
grades.append(grade_changed)

# new desired grades
print("\nGrades Highest to Lowest:")
grades.sort(reverse=True)
for grade in grades:
    print(grade)
print("\n{0}'s Grade Summary:\n ".format(name))
print("Total Number of Grades:", len(grades))
print("Highest Grade:", grades[0])
print("Lowest Grade:", grades[-1])
average_2 = round(sum(grades)/len(grades), 2)
print("Average:", average_2)

# comparison to original grades
print(
    f"\nYour new average would be a {average_2} compared to your real average of {average_1}")
change = round(average_2-average_1, 2)
print(f"That is a change of {change} points!")
print("Too bad your original grades are still the same!")
print(grades_original)
print("You should go ask for extra credit!")

# End of programm.
print("\nThank you for using the Grade Point Average Calculator Application. Goodbye.\n")
print("**"*50)
