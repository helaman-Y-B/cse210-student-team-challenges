from os import system
class Console:

    """
    A code template for a computer console. The responsibility of this 
    class of objects is to get text input and display text output.

    Attributes:
            prompt (string): The prompt to display on each line.
    """

    def read(self, prompt):
        """Gets text input from the user through the Console.

        Args: 
            self (Console): An instance of Console.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Console): An instance of Console.
            text (string): The text to display.
        """
        print(text)

    def clear(self):
        system("cls")
        
