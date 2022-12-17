# Tempreture Converter Application
print("**"*50)

# Welcome message.
print("Welcome To Tempreture Conversion Applicaton.\n")

# Get tempreture in Degree Fehrenheit.
temp_f = float(input("What is the given tempreture in Degree Fehrenheit:"))

# conversion & roundup.
temp_c = round(((5/9)*(temp_f-32)), 4)
temp_k = round((temp_c + 273.15), 4)

# Printing final Result
print("\nDegrees Fehrenheit:\t\t", temp_f)
print("Degrees Celcious:\t\t", temp_c)
print("Degrees Kelvin:\t\t\t", temp_k)

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)
