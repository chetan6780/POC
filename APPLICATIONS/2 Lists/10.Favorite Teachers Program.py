# function 1
def fav_t_info1():
    print("\nYour favorite teachers ranked are:", teachers)
    print("Your favorite teachers ranked alphabetically are:", str(sorted(teachers)))
    print("Your favorite teachers ranked reverse alphabetically are:",
          str(sorted(teachers, reverse=True)))

# function 2
def fav_t_info2():
    print("\nYour top two favorite teachers are:",
          teachers[0], "&", teachers[1])
    print("Your next two favorite teachers are:",
          teachers[2], "&", teachers[3])
    print("Your last favorite teacher is:", teachers[-1])
    print("You have a total of", str(len(teachers)), "favorite teachers.")




# Favorite Teachers Program
print("**"*50)

# Welcome message.
print("Welcome To Favorite Teachers Program.\n")

# creating lists
teachers = []
rank = ["first", "second", "third", "fourth"]
for i in range(0, 4):
    a = rank[i]
    teachers.append(input(f"Who is your {a} favorite teacher:",).title())

# 1
fav_t_info1()
fav_t_info2()

# new favorite teacher
new_fav_t = input(f"\nOops, {teachers[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher:").title()
teachers.insert(0, new_fav_t)

# 2
fav_t_info1()
fav_t_info2()

# remove favorite teacher
rem_fav_t = input("You've decided you no longer like a teacher. Which teacher would you like to remove from you:").title()
teachers.remove(rem_fav_t)

# 3
fav_t_info1()
fav_t_info2()

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)
