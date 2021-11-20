import arcade


class KeyHandler():

    def __init__(self, player):
        self.player = player

    def on_key_press_a(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/K: Move Up, Down
        Arrows: Move Up, Down

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        # if symbol == arcade.key.P:
        #    self.paused = not self.paused
        if symbol == arcade.key.W:
            self.player.change_y = 5

        if symbol == arcade.key.S:
            self.player.change_y = -5

    def on_key_press_b(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/K: Move Up, Down
        Arrows: Move Up, Down

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """

        if symbol == arcade.key.UP:
            self.player.change_y = 5

        if symbol == arcade.key.DOWN:
            self.player.change_y = -5

    def on_key_release_a(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.W
            or symbol == arcade.key.S
        ):
            self.player.change_y = 0

    def on_key_release_b(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0
