class House():
    """A class to model a house that is for sell"""

    def __init__(self, style, sq_footage, year_built, price):
        """Initialize attribute"""
        self.style = style
        self.year_buit = year_built
        self.sq_footage = sq_footage
        self.price = price

        self.sold = False
        self.weeks_on_market = 0

    def disply_info(self):
        """"display the information on the house"""
        print("\n----House for sale----")
        print("House style:\t", self.style)
        print("Square feet:\t", self.sq_footage)
        print("Year built:\t", self.year_buit)
        print("Sale price:\t", self.price)
        print("\nThis house has been on market for",
              self.weeks_on_market, "weeks")

    def sell_house(self):
        """Sell the house"""
        if self.sold == False:
            print("Congratulations! Your hous has been sold for $" +
                  str(self.price)+"!")
            self.sold = True
        else:
            print("Sorry this house is no longer for sell.")

    def change_price(self, amount):
        """Change the sell price of the house"""
        self.price += amount

        if amount < 0:
            print("Price Drop!!!")
        else:
            print("The house has increase in value by $"+str(amount)+".")

    def update_weeks(self, weeks=1):
        """Increment the number of weeks a house has been on market."""
        self.weeks_on_market += weeks


my_house = House("Ranch", 1800.00, 1962, 199000)

"Print out attribute"
print(my_house.style)
print(my_house.sq_footage)
print(my_house.price)
print(my_house.sold)

my_house.disply_info()

# house on market for 1 week
my_house.update_weeks()
my_house.disply_info()

# house on market for 15 week
my_house.update_weeks(15)
my_house.disply_info()

# change the price:drop
my_house.change_price(-15000)
my_house.disply_info()

# hous on market for 5 weeks
my_house.update_weeks(5)
my_house.disply_info()

# new intrest
my_house.change_price(10000)
my_house.disply_info()

# wrong sq_footage
my_house.sq_footage -= 150
my_house.change_price(-1000)
my_house.disply_info()

# sell house
my_house.sell_house()

# agin sell
my_house.sell_house()
