import random
import time

# Defining classes-----------------------------------------------------------------------------------------------------------------------------------------
# class Card.
# class Deck.
# class Player.
# class Dealer.
# class Game.


class Card():
    """The class string the information of cards"""

    def __init__(self, rank, value, suit):
        """Initializing the attribues"""
        self.rank = rank  # 2-10, J, Q, K, A
        self.value = value  # 1-11
        self.suit = suit

    def display_card(self):
        """Displays what card it is"""
        print(f"{self.rank} of {self.suit}.")


class Deck():
    """Built a deck of 52 cards"""

    def __init__(self):
        """Initializing the attributes"""
        self.cards = []

    def build_deck(self):
        """For Building the deck"""
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        # Dict in which key represents the rank of card and value represents the corresponding value of card
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                 '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, }

        for card_name in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, card_name)
                self.cards.append(card)

    def shuffle_deck(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def deal_card(self):
        """remove(get) a card from the deck"""
        card = self.cards.pop()
        return card


class Player():
    """The class of players."""

    def __init__(self):
        """Initializing hte player"""
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        """Draw the card for a palyer"""
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        """Declare players hand"""
        print("\nPlayers hand: ")
        for card in self.hand:
            card.display_card()

    def hit(self, deck):
        """Give the new card to player"""
        card = deck.deal_card()
        self.hand.append(card)

    def get_hand_value(self):
        """calculate the value of palyers hand"""
        self.hand_value = 0
        ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value

        if card.rank == "A":
            ace_in_hand = True

        if self.hand_value > 21 and ace_in_hand:
            # Treat the Ace as if it were 1 instead of 11 by subtracting ten from the
            self.hand_value -= 10

        print("Total value:", self.hand_value)

    def update_hand(self, deck):
        """Update the hand of the player"""
        if self.hand_value < 21:
            choice = input("Would you like to hit(y/n): ").strip().lower()
            if choice == "y":
                self.hit(deck)
            else:
                self.playing_hand = False
        else:
            # The player either has blackjack or is over 21:
            self.playing_hand = False


class Dealer():
    """A class simulating the black jack dealer. They must hit up to 17 and they must reveal their first card."""

    def __init__(self):
        """Initializing the dealer attributes"""
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        """Draw the card for a dealer"""
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        """Display the dealers cards"""
        input("\nPress 'Enter' to reveal dealers hand.")

        # Show all cards in the dealer's hand
        for card in self.hand:
            card.display_card()
            # pause the programm for suspense
            time.sleep(1)

    def hit(self, deck):
        """The dealer must hit until they have reached 17, then they stop."""
        self.get_hand_value()
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print(f"\nDealer is set with a total of {len(self.hand)} cards.")

    def get_hand_value(self):
        self.hand_value = 0

        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "A":
                ace_in_hand = True

        # If the hand’s value greater than 21 and there is an ace in the hand
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10


class Game():
    """A class to hold bets and payouts"""

    def __init__(self, money):
        """Initializing the attributes"""
        self.money = int(money)
        self.bet = 20
        self.winner = ""

    def set_bet(self):
        betting = True
        while betting:
            bet = int(input("what is your bet amount (minimum bet of 20): "))

            if bet < 20:
                bet = 20

            if bet > self.money:
                print("Sorry, you cannot afford the bet.")
            else:
                self.bet = bet
                betting = False

    def scoring(self, player_value, dealer_value):
        """score a round of a blackjack"""

        # any of one got blackjack
        if player_value == 21:
            print("You got BLACK JACK!!! You win!")
            self.winner = "p"
        elif dealer_value == 21:
            print("The dealer got black jack...You loose!")
            self.winner = "d"

        # anyone went over 21
        elif player_value > 21:
            print("Player went over 21! you loose!")
            self.winner = "d"
        elif dealer_value > 21:
            print("Dealer went over 21! you win!")
            self.winner = "p"

        # other cases
        else:
            if player_value > dealer_value:
                print(f"Dealer get's {dealer_value}. You win!")
                self.winner = "p"
            elif dealer_value > player_value:
                print(f"Dealer get's {dealer_value}. You loose!")
                self.winner = "d"
            else:
                print(f"Dealer get's {dealer_value}. it's a push...")
                self.winner = "tie"

    def payout(self):
        """Update the money attribute based on who won a hand."""
        if self.winner == "p":
            self.money += self.bet
        elif self.winner == "d":
            self.money -= self.bet

    def display_money(self):
        """Display the current money"""
        print(f"\nCurrent Money: ₹{self.money}")

    def display_money_and_bet(self):
        """Display the current money and bet for a game round."""
        print(f"\nCurrent Money: ₹{self.money}. \t\tCurrent bet: ₹{self.bet}.")

# defing classes end---------------------------------------------------------------------------------------------------------------------------------------


def main():
    """main code"""

    #  Casino Blackjack Applicaton
    print("**"*50)

    # Welcome message.
    print("Welcome To Casino Blackjack Applicaton.")

    print("\nThe minimum bet at this table is ₹20.")
    money = int(input("How much money are you willing to play with today: "))
    game = Game(money)

    # The main game loop
    playing = True
    while playing:
        # initializing
        game_deck = Deck()
        game_deck.build_deck()
        game_deck.shuffle_deck()

        # define player and dealer
        player = Player()
        dealer = Dealer()

        # display money and set the bet
        game.display_money()
        game.set_bet()

        # Draw the players and dealers hand
        player.draw_hand(game_deck)
        dealer.draw_hand(game_deck)

        # Display the money and bet
        game.display_money_and_bet()

        # reveals the dealers first card.
        print("The dealer is showing a",
              dealer.hand[0].rank, "of", dealer.hand[0].suit)

        # While the player is playing their hand
        while player.playing_hand:
            player.display_hand()
            player.get_hand_value()
            player.update_hand(game_deck)

        # Dealer hit until 17
        dealer.hit(game_deck)
        dealer.display_hand()

        # Winner and payout
        game.scoring(player.hand_value, dealer.hand_value)
        game.payout()

        # If the user has less than the minimum bet of ₹20
        if game.money < 20:
            playing = False
            print("Sorry, you ran out of money. Please try again.")


# If this module is in main module, call the main function
if __name__ == '__main__':
    main()

# End of programm.
    print("\n\nThank you for using the Casino Blackjack Applicaton.Goodbye.\n")
    print("**"*50)
