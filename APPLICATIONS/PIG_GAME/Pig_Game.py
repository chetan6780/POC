import random

# defining classes for program


class Die:
    """Class for the die in dice"""

    def __init__(self):
        self.__value = 1

    @property
    def value(self):
        return self.__value

    def roll(self):
        self.__value = random.randrange(1, 7)


class Game:
    """A Game class for the game"""

    def __init__(self):
        self.turn = 1
        self.score = 0
        self.scoreThisTurn = 0
        self.isTurnOver = False
        self.isGameOver = False
        self.die = Die()

# defining functions for program


def display_welcome():
    print("Let's Play PIG GAME!")
    print()
    print("# See how many turns it takes you to get 20 Points.")
    print("# Turn will end if you hold or roll '1'.")
    print("# If you roll '1', you will lose all poins for that turn.")
    print("# If you hold, you will save all point for the turn.")
    print()


def play_game():
    game = Game()
    while not game.isGameOver:
        take_turn(game)


def take_turn(game):
    print("TURN", game.turn)
    game.scoreThisTurn = 0
    game.isTurnOver = False
    while not game.isTurnOver:
        choice = input("Roll or Hold? (r/h): ").lower()
        if choice.startswith('r'):
            roll_die(game)
        elif choice.startswith('h'):
            hold_turn(game)
        else:
            print("Invalid choice. Please try again.")


def roll_die(game):
    game.die.roll()
    print("Die: ", game.die.value)
    if game.die.value == 1:
        game.scoreThisTurn = 0
        game.turn += 1
        game.isTurnOver = True
        print("Turn over . No score.\n")
    else:
        game.scoreThisTurn += game.die.value


def hold_turn(game):
    game.score += game.scoreThisTurn
    game.isTurnOver = True
    print("Score for turn:", game.scoreThisTurn)
    print("Total score:", game.score, "\n")
    if game.score >= 20:
        game.isGameOver = True
        print("You finishied in", game.turn, "turns!")
    else:
        game.turn += 1


def main():
    display_welcome()
    while True:
        play_game()
        choice = input("Play again? (y/n): ").lower()
        print()
        if not choice.startswith('y'):
            print("Bye!")
            break


# if started as main module, call the main function
if __name__ == '__main__':
    main()
