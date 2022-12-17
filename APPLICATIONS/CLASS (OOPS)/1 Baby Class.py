# class--------->Blueprint to build something
# object-------->What you build
# Instances----->What you work with once it is built
# Attribute----->Information you used to distinguish one instance from other
# Method-------->Behavoir common to all


import random


class Baby():  # only starts with cap letter
    """A simple class to simulate a baby. """

# This is me self
    def __init__(self, name, gender, age):
        """" Initializing attributes"""
        self.name = name.title()
        self.gender = gender
        self.age = age

        self.tired = True

    def play(self):  # These are the methods
        """Simulate playing based on gender"""
        if self.gender == 'male':
            print(self.name, "is playing with cars.")
        else:
            print(self.name, "is playing with blocks")

    def cry(self):
        """Simulate crying"""
        print("WAAAH WAAAH WAAAH!!!")
        print("Even", str(self.age), "year olds cry.")

    def sleep(self):
        """Simulate Sleeping"""
        if self.tired:
            print(self.name, "is sleeping...FINALLY")
            self.tired = False
        else:
            print("sorry", self.name, "is not tired")


# self is getting pass automatically
# here are 4 argument including self not 3

little_boy = Baby('john', 'male', 3)
little_girl = Baby('mary', 'female', 1)  # here are 4 arguments

# -----------------------------------------------------------
# Examles
# print(little_boy.name)
# print(little_girl.name)

# print(little_boy.gender)
# print(little_boy.age)

# print(little_girl.age)
# print(little_boy.tired)
# -----------------------------------------------------------

# print(little_boy.name,"is a",little_boy.age,"year old",little_boy.gender,".")
# print(little_girl.name,"is a",little_girl.age,"year old",little_girl.gender,".")

# little_boy.play()
# little_girl.play()

# little_boy.cry()
# little_girl.cry()

# little_boy.sleep()
# little_girl.sleep()

# little_boy.sleep()
# -----------------------------------------------------------

babies = []
for i in range(25):
    num = random.randint(0, 1)
    if num == 0:
        gender = 'male'
    else:
        gender = 'female'

    age = random.randint(0, 5)

    baby = Baby(str(i), gender, age)
    babies.append(baby)

for baby in babies:
    print("Baby #"+baby.name, "is a", baby.age, "year old", baby.gender+".")

# ---------------------------------------------------------------------
