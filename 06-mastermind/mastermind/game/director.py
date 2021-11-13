from game.console import Console
from game.players import Players
from game.turns import Turns
from game.generator import Generator
from game.comparator import Comparator


class Director:
    """Class Director, its purpouse is to direct every data in our code to the correct class,
    making our code organized and easy to work with.

        Stereotype:
        Direct the data, organize

        Attributes:
        console (class): The class Console from console.py.
        players (class): The class Players from players.py.
        turns (class): The class Turns from turns.py.
        generator (class): The class Generator from generator.py.
        comparator (class): The class Comparator from comparator.py."""

    def __init__(self):
        """The constructor of director."""
        # All classes are called here
        self.console = Console()
        self.players = Players()
        self.turns = Turns()
        self.generator = Generator()
        self.comparator = Comparator()

    def start_game(self):
        """The start_game fuction starts, keeps, and also finneshes the game,
        by sending the correct data to its correct class/function and then 
        resive it back to keep the game running.

        Args:
            self an instance of Director"""

        self.players.set_player1(
            self.console.master_in("Enter a name for player 1: "))  # Calls set_player1 function from Players class and also store user name
        self.players.set_player2(
            self.console.master_in("Enter a name for player 2: "))  # Calls set_player2 function from Players class and also store user name
        self.console.new_line()  # Creates a empty line, to keep the game visualy appeling

        # A loop so that the game keeps going on, until one of the players win
        while self.turns.get_keep():
            # prints a line of '-----------' to keep the game interface beautiful
            self.console.stepper()
            # Show each player their secret codes that they need to guess
            self.console.master_out(
                f"Player {self.players.get_player1()}: {self.generator.get_player1_status()}")
            self.console.master_out(
                f"Player {self.players.get_player2()}: {self.generator.get_player2_status()}")
            self.console.stepper()
            if self.turns.get_turn():
                # This section shows whos turn is
                self.turns.set_current_player(self.players.get_player1())
                turn = self.console.master_in(
                    self.turns.turn_msg(self.players.get_player1()))
                state, comparation, winner, word_state = self.comparator.compare(
                    self.generator.get_player1_code(), turn, self.players.get_wordlist_player1())
                # In case the player guess hasn't already been typed, the following will run
                if word_state:
                    # This section will decide if the user guess is valid or not
                    if state:  # if is valid, the guess will be stored so the player doesn't repeat
                        self.generator.set_player1_state(comparation)
                        self.generator.set_player1_hidden(turn)
                        self.turns.turn_commute()
                        self.console.new_line()
                        self.players.update_wordlist_player1(turn)
                    else:  # If is not valid, it will say that the guess is not valid
                        self.console.master_out(
                            f"{turn} is not a valid input, try again!")
                else:  # If the guess has already happened, then the game will say that the number was already used
                    self.console.master_out(f"You have entered {turn} before")

            else:
                # Here we change the players turn
                self.turns.set_current_player(self.players.get_player2())
                turn = self.console.master_in(
                    self.turns.turn_msg(self.players.get_player2()))
                state, comparation, winner, word_state = self.comparator.compare(
                    self.generator.get_player2_code(), turn, self.players.get_wordlist_player2())

                # And alos do the guess validation for player 2
                if word_state:
                    if state:
                        self.generator.set_player2_state(comparation)
                        self.generator.set_player2_hidden(turn)
                        self.turns.turn_commute()
                        self.console.new_line()
                        self.players.update_wordlist_player2(turn)

                    else:
                        self.console.master_out(
                            f"{turn} is not a valid input, try again!")
                else:
                    self.console.master_out(f"You have entered {turn} before")
            # And in the end, if there is a winner, this part of code will run.
            if winner:
                self.console.master_out(self.turns.win())
                break
