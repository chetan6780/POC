import datetime
import time as t

# Grocery List Application
print("**"*50)

# Creating datetime objects
time = datetime.datetime.now()
year = str(time.year)
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
second = str(time.second)

# Define a grocery list
grocery = ["Meat", "Cheese"]

# Welcome message.
print("Welcome To Grocery List Application.")
print("\nCurrent Date and Time:", day+"/"+month+"/"+year, hour+":"+minute)
print("You currently have", str(grocery[0]), "and", str(
    grocery[1]), "in your list.\n")

# Add food in list
while True:
    items = input("How many items would you like to add:")
    try:
        items=int(items)
        for i in range(0, items):
            grocery.append(input("Type of food to add to the grocery list: ").title())
        break
    except:
        print("Please enter a number.\n")
        continue

# Printing grocery list
print("\nHere is your grocery list:")
print(str(grocery))
grocery.sort()
print("\nHere is your grocery sorted list:")
print(str(grocery))

# Information of current grocery list.
print("\nSimulating grocery shopping.....")

# wait 1 sec
t.sleep(1)

for i in range(0, 3):
    print("\nCurrent grocery list have:", str(len(grocery)), "items")
    print(str(grocery))
    a = input("What food did you just buy:").title().strip()
    print("Removing "+a+" from list.....")
    grocery.remove(a)

print("\nCurrent grocery list have:", str(len(grocery)), "items")
print(str(grocery))
a = input("\nWhat food did you just buy:").title().strip()
grocery.remove(a)

print("\nSorry, the store is out of "+str(a)+".")
b = input("What food would you like instead: ").title().strip()
grocery.append(b)

print("\nHere is what remains on your grocery list:")
print(str(grocery))

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)
