
class Comparator:
    """Comparator class is where we tell the user if they got a correct number
    or got a totally, wrong number from the random number.

    In this case, 'X' means a correct number in a correct position,
    'O' means that there is a correct number, but in the wrong position and,
    '*' means an incorrect number.


            Stereotype:
                        Guess validation, hint deliver.

            Attributes:
                        None.
    """

    def __init__(self):
        """Class constructor.

        Args:
            self an instance of Comparator"""
        pass

    def compare(self, code, user_input, wordlist):
        """Compare Fuction:
                            Compare Function gets 3 different values, called 'code', 'user_input' and 'wordlist'.
                            Code, is the number that the user need to guess,
                            User_input, is the number that the user guessed,
                            wordlist, is a list where each user answer is stored, so that the user don't repeat the same guess again."""

        """Args:
                self an instance of Comparator,
                code, the number the user needs to guess,
                user_input, is the user guess,
                wordlist, where the guesses are stored, so that the user don't repeat them"""

        """Attributes:
                      new_status, which is a list where the hints are stored.
                      winner, which is a boolean value.
                      word_state, which is a boolean value.
                      state, which is also a boolean value."""

        new_status = []  # Store the hints
        winner = False  # The attribute which decide the winner
        word_state = False  # Decide if the guess is new or repeated
        state = False  # Decide if the word is valid or not

        if user_input not in wordlist:
            word_state = True

            if len(user_input) == 4 and user_input.isnumeric():
                state = True
                for i, o in zip(code, user_input):
                    if i in o:
                        new_status.append("X")
                    else:
                        if o in code:
                            new_status.append("O")
                        else:
                            new_status.append("*")

                status = "".join(new_status)
            else:
                status = "----"
                state = False

            if status.count("X") == 4:
                winner = True

        else:
            word_state = False
            state = False
            status = "----"

        return state, status, winner, word_state

# ~ caca = Comparator()
# ~ print(caca.compare("1234", "1111"))
