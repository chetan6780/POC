import math
import random
import tkinter

# Defining classes-----------------------------------------------------------------------------------------------------------------------------------------
# class Simulation
# class Person
# class Population


class Simulation():
    """A class to control simulation"""

    def __init__(self):
        """Initializing attributes"""
        self.day_number = 1
        self.population_size = int(
            input("To simulate an epidemic outbreak. Please enter the population size: "))

        # For visual purposes, we only want a perfect square.so we have to convert it in perfect square if it is not.
        root = math.sqrt(self.population_size)

        # If int(root + 0.5)**2 is not equal to the given population size, then we do not have a perfect square:
        if int(root+0.5)**2 != self.population_size:
            # The reason is that the int function will round the decimal value. If we add 0.5 to the root, unless it is a perfect square, it will always be rounded up and the condition will hold.so make it perfect sqrt by rounding it to 0 decimal places.
            root = round(root, 0)
            self.grid_size = int(root)
            self.population_size = self.grid_size**2

            print(
                f"Rounding the population size to {self.population_size} for visual perposes.")

        else:  # the given population is a perfect square
            self.grid_size = int(math.sqrt(self.population_size))

        print("\nFirst start by infecting a portion of the population.")
        self.infection_percent = float(
            input("---Enter the percentage (0-100) of the population to initially infect: "))
        self.infection_percent /= 100

        print("\nKnowing the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input(
            "---Enter the probability (0-100) that a person gets infected when exposed to the disease: "))

        print("\nknowing how long the infection will last when exposed.")
        self.infection_duration = int(
            input("---Enter the duration (in days) of the infection: "))

        print("\nknowing the mortality rate of those infected.")
        self.mortality_rate = float(
            input("---Enter the mortality rate (0-100) of the infection: "))

        print("\nknowing how long to run the simulation.")
        self.sim_days = int(input("---Enter the number of days to simulate: "))


class Person():
    """A class for the individual person"""

    def __init__(self):
        """Initializing attributes"""
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, simulation):
        """Infecting a person"""
        if random.randint(0, 100) < simulation.infection_probability:
            self.is_infected = True

    def heal(self):
        """Heal a person"""
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        """Kill a person"""
        self.is_dead = True

    def update(self, simulation):
        """update the simulation"""
        # check if a person is not dead.
        if not self.is_dead:
            # check if a person is infected
            if self.is_infected:
                self.days_infected += 1
                # check if a person will die or not
                if random.randint(0, 100) < simulation.mortality_rate:
                    self.die()
                elif self.days_infected == simulation.infection_duration:
                    self.heal()


class Population():
    """A class to model a whole population of Person objects"""

    def __init__(self, simulation):
        """Initializing attributes"""
        self.population = []  # list of N lists.
        # Each list within the list will represent a row in an NxN grid.
        # Each element of the row will represent an individual Person object.
        # Each of these lists will hold N Person objects and there will be N lists.

        for i in range(simulation.grid_size):  # loop through row
            row = []
            # loop trough needed no. of person object for each row
            for j in range(simulation.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)

    def initial_infection(self, Simulation):
        """Infect an initial portion of the population based on initial conditions of the simulation"""
        infected_count = int(
            round(Simulation.infection_percent*Simulation.population_size, 0))

        infections = 0
        while infections < infected_count:
            # x is a random row in the population, y is a random person in the random row
            # self.population[x][y] represents a random person in the population list
            x = random.randint(0, Simulation.grid_size-1)
            y = random.randint(0, Simulation.grid_size-1)

            # now self.population[x][y] represents an individual person in the two dimensional list.
            # If this given person is not infected
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1

    def spread_infection(self, simulation):
        """Spreading the infection in a 2D array to all adjacent people to a given person. 
        A given person in the population attribute is referenced as self.population[i][j] 
        A person to the right of the given person is referenced as self.population[i][j+1] 
        A person to the left of the given person is referenced as self.population[i][j-1] 
        A person below the given person is referenced as self.population[i+1][j] 
        A person above the given person is referenced as self.population[i-1][j]"""

        for i in range(simulation.grid_size):
            # represents each row of the grid
            for j in range(simulation.grid_size):
                # represents an individual Person object in a row.
                if self.population[i][j].is_dead == False:
                    # if a person is alive
                    if i == 0:
                        # first row in population list
                        if j == 0:
                            # first person in first list
                            # we can ckeck for right and below and not left and above person
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size-1:
                            # last person in first list
                            # we can check for left and below not right and above person
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            # we are in any other colomn
                            # we can check to the right, left, and below.
                            if self.population[i][j+1].is_infected or self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    elif i == simulation.grid_size - 1:
                        # last row in population list
                        if j == 0:
                            # first person in last row
                            # we can check for right and above
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size-1:
                            # last person in last row
                            # we can check for left and above
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            # anywhere in list
                            # we can check for left, right, above
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    else:
                        # any row in population list
                        if j == 0:
                            # we are in the first column
                            # we can check for right, below ,above
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size-1:
                            # we are in the last column
                            # we can check for left, below, above
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            # we are in any other column
                            # we can check for left, right,below,above
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)

    def update(self, simulation):
        """Update the whole population by updating each individual Person"""
        simulation.day_number += 1
        for row in self.population:
            # row in the NxN population list
            for person in row:
                # colomn in row(list)
                person.update(simulation)

    def display_statistics(self, simulation):
        """display the statistics of populations"""
        total_infected_count = 0
        total_death_count = 0
        for row in self.population:
            # row in the NxN population list
            for person in row:
                # colomn in row(list)
                # check if a person is infected or dead
                if person.is_infected:
                    total_infected_count += 1
                    if person.is_dead:
                        total_death_count += 1

        # Calculate percentage of population that is infected and dead
        infected_percent = round(
            100*(total_infected_count/simulation.population_size), 4)
        death_percent = round(
            100*(total_death_count/simulation.population_size), 4)

        # Summery
        print(f"\n----- Day #{simulation.day_number} -----")
        print(f"Percentage of Population Infected: {infected_percent}%")
        print(f"Percentage of Population Dead: {death_percent}%")
        print(
            f"Total People Infected: {total_infected_count} / {simulation.population_size}")
        print(
            f"Total Deaths: {total_death_count} / {simulation.   population_size}")

# Defining classes end-------------------------------------------------------------------------------------------------------------------------------------
# Defining functions------------------------------------------------------------------------------------------------------------------------------------


def graphics(simulation, population, canvas):
    """A helper function to update the tkinter display."""
    # To get the dimensions of a square, we can take the dimensions of the window and divide by total number of squares in a row.
    # 600x600 in my case ,change if desire
    # Each square represents a person in the population

    square_dimension = 800//simulation.grid_size  # floor division
    # loop through all possible rows of the grid
    for i in range(simulation.grid_size):
        y = i*square_dimension
        # loop through in the raw
        for j in range(simulation.grid_size):
            x = j*square_dimension

            # if the given person is dead
            if population.population[i][j].is_dead:
                # create red rectangle
                canvas.create_rectangle(
                    x, y, x + square_dimension, y + square_dimension, fill="red")
            else:
                if population.population[i][j].is_infected:
                    # create yellow rectangle
                    canvas.create_rectangle(
                        x, y, x + square_dimension, y + square_dimension, fill="yellow")
                else:
                    # create green rectangle
                    canvas.create_rectangle(
                        x, y, x + square_dimension, y + square_dimension, fill="green")


def main():
    """main code"""
    #  Epidemic Outbreak GUI Applicaton
    print("**"*50)

    # Welcome message.
    print("Welcome To Epidemic Outbreak GUI Applicaton.")

    # simulation object
    sim = Simulation()

    # tkinter objects
    sim_window = tkinter.Tk()
    sim_window.title("Epidemic Outbreak")
    sim_canvas = tkinter.Canvas(sim_window, width=600, height=600, bg='white')
    sim_canvas.pack(side=tkinter.LEFT)

    # A Population object.
    pop = Population(sim)

    # initializing
    pop.initial_infection(sim)
    pop.display_statistics(sim)
    input("Press 'Enter' to start simulation")

    # Simulation
    for i in range(1, sim.sim_days):
        # Spread the infection
        pop.spread_infection(sim)
        # Update the population
        pop.update(sim)
        # Display the statistics
        pop.display_statistics(sim)
        # Show the graphics
        graphics(sim, pop, sim_canvas)
        # update the window
        sim_window.update()
        
        # If we are currently not on the last day of the simulation:
        if i != sim.sim_days-1:
            sim_canvas.delete("all")

    # End of programm.
    print("\n\nThank you for using the Epidemic Outbreak GUI Applicaton. Goodbye.\n")
    print("**"*50)


if __name__ == "__main__":
    main()
