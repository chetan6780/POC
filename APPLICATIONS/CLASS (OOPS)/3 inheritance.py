# Inheritance

# parent class to ----------> child class

# The parent class


class Dog():
    """A class to represent the genral dog"""

    def __init__(self, name, gender, age, louad):
        """Initialize the attributes"""
        self.name = name.title()
        self.gender = gender
        self.age = age
        self.is_loud = louad  # loud is bool

    def call_dog(self):
        """call the dog"""
        if self.gender == "male":
            print(f"here {self.name}! Good boy!")
        else:
            print(f"here {self.name}! Good girl!")

    def dog_years(self):
        """Compute age in dog years"""
        dog_years = self.age*7
        print(f"{self.name} is {dog_years} years old in dog years.")

    def bark(self):
        """Get the dog to speek"""
        if self.is_loud:
            print("WOOF WOOF WOOF!!")
        else:
            print("woof!")

# A child class Beagle


class Beagle(Dog):
    """A class to represent a specific type of dog"""

    def __init__(self, name, gender, age, louad, gunshy):# added gushy
        """ Initialize attribute of parent class"""
        super().__init__(name, gender, age, louad)
        self.is_gunshy=gunshy # a bool

    def bark(self):
            """Get the dog to speek"""
            if self.is_loud:
                print("HOOOOWWWWWLLLLLL!!")
            else:
                print("howl!")
    
    def go_hunt(self):
        """if the dog is not gunshy, take them gunting"""
        if not self.is_gunshy:
            self.bark()
            print(f"{self.name} just brought back a duck.")
        else:
            print(f"{self.name} is not a good hunting dog.")

class Chihuahua(Dog):
    """represents a specufic type of dog"""

    def __init__(self, name, gender, age, louad):
        """intlz attribute for the parent class"""
        super().__init__(name, gender, age, louad)

    def bark(self):
       if self.is_loud:
            print("YIP YIP YIP YIP YIP YIP")
       else:
            print("yip")


my_dog = Dog('spark', 'male', 3, True)
print(my_dog.name)
print(my_dog.age)

my_dog.call_dog()
my_dog.dog_years()
my_dog.bark()

your_dog = Beagle("lassi", "female", 8, False,False)

print(type(my_dog))
print(type(your_dog))

your_dog.call_dog()
your_dog.dog_years()
your_dog.bark()

your_dog.go_hunt()
# my_dog.go_hunt() # no atrribute 

tiny_dog=Chihuahua("tiny","male",2,True)
tiny_dog.call_dog()
tiny_dog.dog_years()
tiny_dog.bark()

# tiny_dog.go_hunt()
