from math import *

# Right triangle solver application.
print("**"*50)

# Welcome message.
print("Welcome To Right triangle solver Application.\n")

# input side of triangles.
s1 = float(input("What is first side of triangle:"))
s2 = float(input("What is second side of triangle:"))

# calculation of hypotenuse and area.
s3 = round((sqrt(s1**2+s2**2)), 3)
Area = round((0.5*s1*s2), 3)

# Showing results.
print("\nFor a triangle with legs of {0} and {1} the hypotenuse is {2}.".format(s1, s2, s3))
print("For a triangle with legs of {0} and {1} the Area is {2}.".format(s1, s2, Area))

# End of programm.
print("\nThank you for using this application!\n")
print("**"*50)
