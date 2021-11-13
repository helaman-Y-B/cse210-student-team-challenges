
class Console:
    """ A simple console code.
    class responsibility: display text on the standart output and return inputs

        Stereotype:
        Service Provider, Interfacer

        Attributes: 
        -welcome: to display a message when game start.

    """

    def __init__(self):
        # Prints a welcome message.
        welcome = """ 
        
                      _                          
        __      _____| | ___ ___  _ __ ___   ___ 
        \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \\
         \ V  V /  __/ | (_| (_) | | | | | |  __/
          \_/\_/ \___|_|\___\___/|_| |_| |_|\___|

        """

        print(welcome)

    def master_out(self, output_value):
        """Master_out prints the user name.

        Args:
            self an instance of Director,
            output_value, the user name."""
        # displays user name
        print(output_value)

    def master_in(self, message):
        """Master_in returns the user name.

        Args:
            self an instance of Director,
            message, the question for the user name"""
        # returns an input given by the user
        x = input(message)
        return x

    def stepper(self):
        """stepper prints a string to make the game look visualy appeling.

        Args:
            self an instance of Director"""
        # prints the string "--------------------"
        print("--------------------")

    def new_line(self):
        """new_line prints a new line.

        Args:
            self an instance of Director"""
        # prints a new line
        print()
