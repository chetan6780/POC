import random

# defining classes-----------------------------------------------------------------------------------------------------------------------------------------


class Pykemon():
    """Parent class in which the child classes Fire, Water,and Grass"""

    def __init__(self, name, element, health, speed):
        """Initializing attributes"""
        self.name = name.title()
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True

    def light_attack(self, enemy):
        """Light attack which create the ASSURED minimum damage"""
        # Create damage
        damage = random.randint(15, 25)
        # All pykemon will have a list moves = [light, heavy, restore, special] all light attacks are at index 0
        print(f"Pykemon {self.name} used {self.moves[0]}.")
        print(f"It dealt with {damage} damage.")

        # Raduces the enemy's health
        enemy.current_health -= damage

    def heavy_attack(self, enemy):
        """Heavy attack which create MASSIVE or no damage"""
        # Create damage
        damage = random.randint(0, 50)
        # All pykemon will have a list moves = [light, heavy, restore, special] all heavy attacks are at index 1
        print(f"Pykemon {self.name} used {self.moves[1]}.")

        if damage < 10:
            print("The attack missed.")
        else:
            print(f"It dealt with {damage} damage.")
            # Raduces the enemy's health
            enemy.current_health -= damage

    def restore(self):
        """Restores the current health"""
        # Restore the health
        heal = random.randint(15, 25)
        # All pykemon will have a list moves = [light, heavy, restore, special] all restore moves are at index 2
        print(f"Pykemon {self.name} used {self.moves[2]}.")

        print(f"It healed {heal} health points.")
        # Increases health
        self.current_health += heal

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def faint(self):
        """if pykemon run out of health, the pykemon faint..."""
        if self.current_health <= 0:
            self.is_alive = False
            print(f"Pykemon {self.name} has fainted!")
            input("Press 'Enter' to continue.")

    def show_stats(self):
        """Display the current stats of pykemon"""
        print(f"\nName: {self.name}")
        print(f"Element Type: {self.element}")
        print(f"Health: {self.current_health} / {self.max_health}")
        print(f"Speed: {self.speed}")


class Fire(Pykemon):
    """A Fire based pykemon that is a child of the Pykemon parent class."""

    def __init__(self, name, element, health, speed):
        """Initialize attributes"""
        super().__init__(name, element, health, speed)

        # List of moves for Fire type Pykemon
        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast']

    def special_attack(self, enemy):
        """
        FIRE BLAST: an elemental fire move. 
        Massive damage to grass type, 
        normal damage to fire type, 
        minimal damage to water type.
        """
        # All pykemon will have a list moves = [light, heavy, restore, special] all special moves are at index 3
        print(f"Pykemon {self.name} used {self.moves[3].upper()}!")

        # Generate damage based on enemy type of pykemon
        if enemy.element == 'GRASS':
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == 'WATER':
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            random.randint(10, 30)

        # Deal damage
        print(f"It dealt {damage} damage.")
        enemy.current_health -= damage

    def move_info(self):
        """Display the information of moves"""
        print(f"\n{self.name} Moves: ")

        # Light attack
        print(f"-- {self.moves[0]} --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print(f"-- {self.moves[1]} --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # Restore move
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")

        # Special attack
        print(f"-- {self.moves[3]} --")
        print("\tA powerful FIRE based attack...")
        print("\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon.")


class Water(Pykemon):
    """A Water based pykemon that is a child of the Pykemon parent class."""

    def __init__(self, name, element, health, speed):
        """Initialize attributes from the parent Pykemon class."""
        super().__init__(name, element, health, speed)

        # list of moves unique to all Water type Pykemon
        self.moves = ['Bite', 'Splash', 'Dive', 'Water Cannon']

    def special_attack(self, enemy):
        """
        WATER CANNON: an elemental water move. 
        Massive damage to fire type,
        normal damage to water type, 
        minimal damage to grass type.
        """
        print("Pykemon {self.name} used {self.moves[3].upper()}!")

        # damage based on enemy type
        if enemy.element == 'FIRE':
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == 'GRASS':
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            random.randint(10, 30)

        # Deal damage
        print(f"It dealt {damage} damage.")
        enemy.current_health -= damage

    def move_info(self):
        """Display the information of moves"""
        print("\n" + self.name + " Moves: ")

        # Light attack
        print(f"-- {self.moves[0]} --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print(f"-- {self.moves[1]} --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # Restore move
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")

        # Special attack
        print(f"-- {self.moves[3]} --")
        print("\tA powerful WATER based attack...")
        print("\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")


class Grass(Pykemon):
    """A Grass based pykemon that is a child of the Pykemon parent class."""

    def __init__(self, name, element, health, speed):
        """Initialize attributes from the parent Pykemon class."""
        super().__init__(name, element, health, speed)
        # Move list unique to all Grass type Pykemon
        self.moves = ['Vine Whip', 'Wrap', 'Grow', 'Leaf Blade']

    def special_attack(self, enemy):
        """LEAF BLADE: an elemental grass move. 
        Massive damage to water type,
        normal damage to grass type, 
        minimal damage to fire type."""
        print(f"Pykemon {self.name} used {self.moves[3].upper()}!")

        # damage based on enemy type
        if enemy.element == 'WATER':
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == 'FIRE':
            print("It's not very effective...")
            damage = random.randint(5, 10)
        else:
            random.randint(10, 30)

        # Deal damage
        print(f"It dealt {damage} damage.")
        enemy.current_health -= damage

    def move_info(self):
        """Display pykemon move info"""
        print(f"\n{self.name} Moves: ")

        # Light attack
        print(f"-- {self.moves[0]} --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print(f"-- {self.moves[1]} --")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # Restore move
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")

        # Special attack
        print(f"-- {self.moves[3]} --")
        print("\tA powerful GRASS based attack...")
        print("\tGuaranteed to deal MASSIVE damage to WATER type Pykemon.")


class Game():
    """A game object to control the creation and flow of pykemon and simulate battle!"""

    def __init__(self):
        """Initialize attributes"""

        # element and name will be chosen randomly at the starting.
        self.pykemon_elements = ['FIRE', 'WATER', 'GRASS']
        self.pykemon_names = ['Chewdie', 'Spatol', 'Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil',
                              'Jampot', 'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur']

        # no battles are won at the starting.
        self.battles_won = 0

    def create_pykemon(self):
        """To Randomly generate a Pykemon!"""

        # Randomly generates health and speed attributes
        health = random.randint(70, 100)
        speed = random.randint(1, 10)

        # Randomly chooses an element and name
        element = self.pykemon_elements[random.randint(
            0, len(self.pykemon_elements)-1)]
        name = self.pykemon_names[random.randint(0, len(self.pykemon_names)-1)]

        # Create the right elemental pykemon
        if element == 'FIRE':
            pykemon = Fire(name, element, health, speed)
        elif element == 'WATER':
            pykemon = Water(name, element, health, speed)
        else:
            pykemon = Grass(name, element, health, speed)
        return pykemon

    def choose_pykemon(self):
        """A method to simulate choosing a starting Pykemon similar to Pokemon"""
        # list of 3 pykemon to start
        starters = []

        # Picks 3 different elemental type pykemon from the starter list
        while len(starters) < 3:
            # creates sarter pykemon
            pykemon = self.create_pykemon()

            # Bool to determine if pykemon is unique and should be added to the starters list
            valid_pykemon = True

            for starter in starters:
                # if the name or element is already used by another starter
                if starter.name == pykemon.name or starter.element == pykemon.element:
                    valid_pykemon = False

            # if The created pykemon is unique, add it to the list starter
            if valid_pykemon:
                starters.append(pykemon)

        # shows the starter pykemon
        for starter in starters:
            starter.show_stats()
            starter.move_info()

        # information of pykemon
        print("\nProfessor Eramo presents you with three Pykemon: ")
        print(f"(1) - {starters[0].name}")
        print(f"(2) - {starters[1].name}")
        print(f"(3) - {starters[2].name}")

        choice = int(input("Which Pykemon would you like to choose: "))
        pykemon = starters[choice-1]

        return pykemon

    def get_attack(self, pykemon):
        """Get a users attack choice"""

        # move list
        print("\nWhat would you like to do...")
        print(f"(1) - {pykemon.moves[0]}")
        print(f"(2) - {pykemon.moves[1]}")
        print(f"(3) - {pykemon.moves[2]}")
        print(f"(4) - {pykemon.moves[3]}")
        choice = int(input("Please enter your move choice: "))

        # Formatting
        print("\n"+("-"*30))
        return choice

    def player_attack(self, move, player, computer):
        """Attack on computer """

        # attack method based on the given move
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)

        # if the computer has fainted
        computer.faint()

    def computer_attack(self, player, computer):
        """Computer AI attack the player"""
        # Randomly pick a move for the computer to execute
        move = random.randint(1, 4)

        # attack method based on the given move
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)

        # if the player has fainted
        player.faint()

    def battle(self, player, computer):
        """Simulate a battle round. Faster Pykemon go first."""
        # players move for the round
        move = self.get_attack(player)

        # If the player's pykemon is faster than the computer, they go first
        if player.speed >= computer.speed:
            self.player_attack(move, player, computer)
            if computer.is_alive:
                # Computer is still alive, let them attack
                self.computer_attack(player, computer)

        # else The player's pykemon is slower than the computer, the computer goes first
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                # Player is still alive, let them attack
                self.player_attack(move, player, computer)

# classes end----------------------------------------------------------------------------------------------------------------------------------------------


def main():
    """tha main code"""
    #  Pykemon Simulator Applicaton
    print("**"*50)

    # Welcome message.
    print("Welcome To Pykemon Simulator Applicaton.")
    print("Can you become the worlds greatest Pykemon Trainer???")
    print("\nDon't worry! Prof Eramo is here to help you on your quest.")
    print("He would like to gift you your first Pykemon!")
    print("Here are three potential Pykemon partners.")
    input("Press 'Enter' to choose your Pykemon!")

    # The main game loop
    playing_main = True
    while playing_main:
        # game instance
        game = Game()

        # starter pykemon
        # print("------")  # for debugging
        player = game.choose_pykemon()
        # print("------")  # for debugging
        print(f"\nCongratulations Trainer, you have chosen {player.name}!")
        input(f"\nYour journey with {player.name} begins now...Press 'Enter'!")

        # While pykemon is alive, continue to do battle
        while player.is_alive:
            # computer pykemon to battle
            computer = game.create_pykemon()
            print(f"\nOH NO! A wild {computer.name} has approached!")
            computer.show_stats()

            # While this enemy pykemon is alive and the player pykemon is alive,engage in battle
            while computer.is_alive and player.is_alive:
                game.battle(player, computer)

                # Both parties survived a round, shows their current stats
                if computer.is_alive and player.is_alive:
                    player.show_stats()
                    computer.show_stats()

            # If the player survived the battle, increment battles_won
            if player.is_alive:
                game.battles_won += 1

        # Formatting
        print("--"*15)

        # The player has finally fainted
        print(f"\nPoor {player.name} has fainted...")
        print(f"But not before defeating {game.battles_won} Pykemon!")

        # Ask the user if they want to play again
        choice = input("Would you like to play again (y/n): ").lower()
        if choice != 'y':
            playing_main = False
            print("Thank you for playing Pykemon!")

        # End of programm.
        print("\n\nThank you for using the Pykemon Simulator Applicaton. Goodbye.\n")
        print("**"*50)


if __name__ == '__main__':
    main()
