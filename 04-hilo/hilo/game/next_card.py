import random

class Dealer_card:
    """Dealer_card class is used to 'Throw' a card
        so that the game can start, continue and end the game."""
    """Attributes:
                card and cards"""

    def __init__(self):
        """The class constructor.

        Args: 
            self (Dealer_card): an instance of Dealer_card."""

        # self.cards is the list of the 13 possible cards that the dealer can throw.
        self.cards = [1, 2, 3, 4, 5, 6,
                      7, 8, 9, 10, 11, 12, 13]
        # declared player response to get higher or lower inputs
        self.player_response = ""

    def get_points(self, next_card, current_card):
        """The get_points method calculates and returns the total points for the current game. 
        It goes from 1 point up until 13 points
        
        Args:
            self (Dealer_card): an instance of Dealer_card.
            next_card: the value of the next card from the throw_card
            current_card: the value of the current card from the throw_card
        Return:
            points: returning the points for getting the result from the comparison
        """

        points = 0

        #evaluating response from the user
        if (self.player_response == "l" and next_card < current_card) or (self.player_response == "h" and next_card > current_card):
            points = 100
        elif (self.player_response == "l" and next_card > current_card) or (self.player_response == "h" and next_card < current_card):
            points = -75
        elif next_card == current_card:
            print("Current Card and Next Card is equal. No score added.")
        else:
            print("Invalid Response! Please enter 'h' or 'H' for Highest or 'l' or 'L' for Lowest")
            
        return points

    def throw_card(self):
        """The throw_card method randomly choose a value from a list called 'cards'. 

        Args:
            self (Dealer_card): an instance of Dealer_card. 
        Return:
            card: return the randomly choosen card and use as playing cards"""
        
        # Randomly choose a card from the cards list
        card = random.choice(self.cards)

        return card