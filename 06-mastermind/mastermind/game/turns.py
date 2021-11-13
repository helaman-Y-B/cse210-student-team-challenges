class Turns:
    """A code template for the turns of the player.
    
    Attributes: 
        keep_playing(Boolean): if the player status is keep on playing
        turn_relay (Boolean): continue to relay the turn
        current_player (String): current player
    """
    def __init__(self):
        """Class constructor. Declare and initializes instance attributes.
        
        Args:
            self (Turns): An instance of Turns.
        """
        self.__keep_playing = True
        self.__turn_relay = True
        self.__current_player = ""
        
    def get_keep(self):
        """Getter of keep playing.
        
        Args: 
            self (Turns): An instance of Turns.
        Return:
            self.__keep_playing (Boolean): return true or false if the player keep on playing or not
        """
        return self.__keep_playing
    
    def turn_msg(self, name):
        """Give a message for the player guesses.

        Args:
            self (Turns): An instance of Turns.

        Return:
            message (string): the message to be displayed.    
        """
        message = f"{name}'s turn: \nWhat is your guess? "
        return message
    
    def turn_commute(self):
        """evaluate the turn_relay and store a boolean value
        
        Args: 
            self (Turns): An instance of Turns.
        """
        if self.__turn_relay:
            self.__turn_relay = False
        else:
            self.__turn_relay = True
    
    def get_turn(self):
        """Getter of the turn
        
        Args:
             self (Turns): An instance of Turns.
        
        Return:
            self.__turn_relay (boolean): continue to relay the turn
        """
        return self.__turn_relay
        
    def set_current_player(self, value):
        """Set the current player
        
        Args:
            self (Turns): An instance of Turns.
            value(string): the name of the player
        """
        self.__current_player = value
    
    def win(self):
        """message if the player won the game
        
        Args:
            self (Turns): An instance of Turns.
        
        Return:
            message (string): the message that player won the game.
        """
        message = f"{self.__current_player} won! "
        return message
    
        
        
        
        
