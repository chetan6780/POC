import random

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
        self.population = []  # list of all person instances

        for i in range(simulation.population_size):  # loop through row
            person = Person()
            self.population.append(person)

    def initial_infection(self, Simulation):
        """Infect an initial portion of the population based on initial conditions of the simulation"""
        infected_count = int(
            round(Simulation.infection_percent*Simulation.population_size, 0))

        for i in range(infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1

        # shuffle the population to spred the infection
        random.shuffle(self.population)

    def spread_infection(self, simulation):
        """Spreading the infection in list population"""
        for i in range(len(self.population)):
            if self.population[i].is_dead == False:
                # if a person is not dead
                if i == 0:
                    # first person in list
                    # check for right
                    if self.population[i+1].is_infected:
                        self.population[i].infect(simulation)
                elif i < len(self.population)-1:
                    # middle person in list
                    # check for right and left
                    if self.population[i-1].is_infected or self.population[i+1].is_infected:
                        self.population[i].infect(simulation)
                elif i == len(self.population)-1:
                    # last person in a list
                    # check for left
                    if self.population[i-1].is_infected:
                        self.population[i].infect(simulation)

    def update(self, simulation):
        """Update the whole population by updating each individual Person"""
        simulation.day_number += 1
        for person in self.population:
            person.update(simulation)

    def display_statistics(self, simulation):
        """display the statistics of populations"""
        total_infected_count = 0
        total_death_count = 0
        for person in self.population:
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
        print(f"\n-----Day #{simulation.day_number} -----")
        print(f"Percentage of Population Infected: {infected_percent}%")
        print(f"Percentage of Population Dead: {death_percent}%")
        print(
            f"Total People Infected: {total_infected_count} / {simulation.population_size}")
        print(
            f"Total Deaths: {total_death_count} / {simulation.   population_size}")

    def graphics(self):
        """Graphical representation: 0 is healthy,I is infected,X is dead"""
        status = []
        for person in self.population:
            # if person is dead
            if person.is_dead:
                char = "X"
            else:
                # person is alive
                # if he/she infected or healthy
                if person.is_infected:
                    char = "I"
                else:
                    char = "0"

            status.append(char)

        # print status separeted by -
        for letter in status:
            print(letter, end="-")

# Defining classes end-------------------------------------------------------------------------------------------------------------------------------------
# Defining functions------------------------------------------------------------------------------------------------------------------------------------


def main():
    """main code"""
    #  Epidemic Outbreak Terminal Applicaton
    print("**"*50)

    # Welcome message.
    print("Welcome To Epidemic Outbreak Terminal Applicaton.")

    # simulation object
    sim = Simulation()

    # A Population object.
    pop = Population(sim)

    # initializing
    pop.initial_infection(sim)
    pop.display_statistics(sim)
    pop.graphics()
    input("Press 'Enter' to start simulation")

    # Simulation
    for i in range(1, sim.sim_days):
        # Spread the infection
        pop.spread_infection(sim)
        # Update the population
        pop.update(sim)
        # Display the statistics
        pop.display_statistics(sim)
        pop.graphics()

        # If we are currently not on the last day of the simulation:
        if i != sim.sim_days-1:
            input("\nPress 'Enter' to advance to the next day.")

    # End of programm.
    print("\n\nThank you for using the Epidemic Outbreak Terminal Applicaton. Goodbye.\n")
    print("**"*50)


if __name__ == "__main__":
    main()
