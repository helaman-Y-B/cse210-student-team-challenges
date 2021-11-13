from random import randint

class Generator:
    """A code template for a number and text generator. Also this is a class where the getter and setter are taking place.

    Attributes:
        player1_code (integer): random number between 1000 to 9999 for player 1
        player2_code (integer): random number between 1000 to 9999 for player 2
        player1_state (string): holder of the last number inputted by the player
        player2_state (string): holder of the last number inputted by the player
        player1_hidden (string): to hide the code or random number
        player2_hidden (string): to hide the code or random number
    """
    
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.
        
        Args:
            self (Generator): An instance of Generator.
        """
        self.__player1_code = randint(1000, 9999)
        self.__player2_code = randint(1000, 9999)
        self.__player1_state = "****"
        self.__player2_state = "****"
        self.__player1_hidden = "----"
        self.__player2_hidden = "----"
        
    def get_player1_status(self):
        """Form initial status of the player of the state and hidden
        
        Args:
            self (Generator): An instance of Generator.
        
        Return:
            status (string): return a set of string of the initial state and hidden form
        """
        status = f"{self.__player1_hidden}, {self.__player1_state}"
        return status
    
    def get_player2_status(self):
        """Form initial status of the player of the state and hidden
        
        Args:
            self (Generator): An instance of Generator.
        
        Return:
            status (string): return a set of string of the initial state and hidden form
        """
        status = f"{self.__player2_hidden}, {self.__player2_state}"
        return status
 
    def get_player1_code(self):
        """Getter of random generated value of the player
        
        Args:
            self (Generator): An instance of Generator.
        
        Return:
            status (string): Return a random generated value of the player
        """
        return str(self.__player1_code)
    
    def get_player2_code(self):
        """Getter of random generated value of the player
        
        Args:
            self (Generator): An instance of Generator.
        
        Return:
            status (string): Return a random generated value of the player
        """
        return str(self.__player2_code)
        
    def set_player1_state(self, value):
        """Set value from the player
        
        Args: 
            self (Generator): An instance of Generator.
            value(String): entered value by the player
        """
        self.__player1_state = value
    
    def set_player2_state(self, value):
        """Set value from the player
        
        Args: 
            self (Generator): An instance of Generator.
            value(String): entered value by the player
        """
        self.__player2_state = value
    
    def set_player1_hidden(self, value):
        """Set value from the player turn
        
         Args: 
            self (Generator): An instance of Generator.
            value(String): entered value by the player
        """
        self.__player1_hidden = value
    
    def set_player2_hidden(self, value):
        """Set value from the player turn
        
         Args: 
            self (Generator): An instance of Generator.
            value(String): entered value by the player
        """
        self.__player2_hidden = value
