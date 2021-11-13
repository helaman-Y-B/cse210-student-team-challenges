
class Players:
    """ A simple piece of code created to manage players.
    class responsibility: store and return player names
    
        Stereotype:
        Service Provider
        
        Attributes: 
        __player1 (String): stores a player's name
        __player2 (String): stores a player's name
        __wordlist_player1 (list): list of value entered by the player
        __wordlist_player2 (list): list of value entered by the player
    """
    
    def __init__(self):
        """
        The class constructor. Declare and initializes instance attributes.

        Args:
            self (Players): An instance of Players
        """
        
        self.__player1 = "player1"
        self.__player2 = "player2"
        self.__wordlist_player1 = []
        self.__wordlist_player2 = []
        
    def get_player1(self):
        """Getter for the value of the player1
        
        Args:
            self (Players): An instance of Players
        
        Return:
            self.__player1 (string): Return the name of the player
        """
        return self.__player1

    def get_player2(self):
        """Getter for the value of the player2
        
        Args:
            self (Players): An instance of Players
        
        Return:
            self.__player2 (string): Return the name of the player
        """
        return self.__player2

    def set_player1(self, player):
        """Setting the name of the player
        
        Args:
            self (Players): An instance of Players
            player(string): The name entered by the player
        """
        self.__player1 = player

    def set_player2(self, player):
        """Setting the name of the player
        
        Args:
            self (Players): An instance of Players
            player(string): The name entered by the player
        """
        self.__player2 = player
        
    def get_wordlist_player1(self):
        """To return the value entered by the player.
        
        Args:
            self (Players): An instance of Players        
        
        Return:
            self.__wordlist_player1 (list): list of value entered by the player
        """
        return self.__wordlist_player1

    def get_wordlist_player2(self):
        """To return the value entered by the player.
        
        Args:
            self (Players): An instance of Players        
        
        Return:
            self.__wordlist_player2 (list): list of value entered by the player
        """
        return self.__wordlist_player2
    
    def update_wordlist_player1(self, word):
        """Update the list of the __wordlist_player1 by adding the value to the list
        
        Args:
            self (Players): An instance of Players
            word (integer): Value entered by the player     
        """
        self.__wordlist_player1.append(word)

    def update_wordlist_player2(self, word):
        """Update the list of the __wordlist_player1 by adding the value to the list
        
        Args:
            self (Players): An instance of Players
            word (integer): Value entered by the player     
        """
        self.__wordlist_player2.append(word)

