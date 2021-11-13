from game.next_card import Dealer_card

class Dealer:
    def __init__(self):
        """The class constructor.
        Args:
            self (Dealer): an instance of Dealer.
        """
        # keep_playing is = to True, so that the game can start
        self.keep_playing = True
        # The user score
        self.score = 300
        # calls the Dealer_card class.
        self.next_card = Dealer_card()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.init_card = self.next_card.throw_card()
        self.current_card = ""
        self.final_score = 0

        while self.keep_playing:
            """Functions to start the game"""
            # Calls the output functions, making the game start
            self.output(self.init_card) 

            #Evaluating if the score is zero or not
            if self.score == 0:
                #if the score is zero, it is game over and end of the game.
                print("=============================================================================")
                print("GAME OVER! \nThank you for you time playing this game. \nWe hope you have fun")
                print("=============================================================================")
                break
            else:
                #Else we will ask for the user if they wanted to play or not.
                play = input("Keep Playing? [y/n]")
                if "n" in play:
                    print("Thank you for playing with us. Have a nice day!")
                    break
        
    def updates(self, next_card):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.
        Args:
            self (Dealer): an instance of Dealer.
            next_card: variable that store the next card for the game
        Return:
            final_score: return updated scores
        """
        # calls the get_points function from Dealer_card class, and store  the points into a value called score
        points = self.next_card.get_points(next_card, self.current_card)
        final_score = self.score + points
        
        return final_score

    def output(self, init_card):
        """Outputs the important game information for each round of play. In 
        this case, that means the card that were showed and the score.
        Args:
            self (Dealer): an instance of Dealer.
            init_card: the inital card 
        """
        #storing card from the Dealer_card class to store as a next_card
        next_card = self.next_card.throw_card()
        #Storing initial card as the current card for the comparison purposes
        self.current_card = init_card
        print(f"\nThe Card is: {init_card}")

        #asking the player for his/her guess.
        choice = input("Higher or Lower? [H/L] ").lower()
        #getting the response of the player
        self.next_card.player_response = choice
        
        #Showing the next card
        print(f"Next Card was: {next_card}")
        #Update of scores and storing the return of the update function.
        self.score = self.updates(next_card)

        #printing of the current score
        print(f"Your current score is: {self.score}")

        #Getting the value of next_card to be used as a parameter
        self.init_card = next_card