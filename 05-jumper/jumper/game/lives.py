class Lives:
    """Lives class have the responssabilitie to track and update the player lives.

    Stereotype:
        Number of lives left.

       Attributes:
                Lives(Interger), the number of lives from the current player."""

    def __init__(self) -> None:
        """The class constructor

        Args:
            self (Lives): an instance of the class Lives.

        Here we also store the number of lives, in our case we will start with 4 lives.
        """
        self.lives = 4

    def lives_counter(self, user_guess):
        """Here is were it will decide, if the player lost a life, or he will keep with the life.

        Args:
            self (Lives): an instance of the class Lives.
            user_guess (Boolean): A Boolean which if it is false, it will remove 1 life of the player."""

        if user_guess == False:
            self.lives -= 1
            return self.lives

        elif user_guess == True:
            self.lives = self.lives
            return self.lives
