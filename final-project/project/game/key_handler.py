import arcade


class KeyHandler():

    def __init__(self, player):
        self.player = player

    def on_key_press_a(self, symbol, modifiers, power):
        """Handle user keyboard input from player 1
        Q: Quit the game
        P: Pause/Unpause the game
        W/S: Move Up, Down

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if power == "no power":
            if symbol == arcade.key.W:
                self.player.change_y = 5

            if symbol == arcade.key.S:
                self.player.change_y = -5

        elif power == "green":
            if symbol == arcade.key.W:
                self.player.change_y = -5

            if symbol == arcade.key.S:
                self.player.change_y = 5

    def on_key_press_b(self, symbol, modifiers, power):
        """Handle user keyboard input from player 2
        Q: Quit the game
        P: Pause/Unpause the game
        W/S: Move Up, Down
        Arrows: Move Up, Down

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if power == "no power":
            if symbol == arcade.key.UP:
                self.player.change_y = 5

            if symbol == arcade.key.DOWN:
                self.player.change_y = -5

        elif power == "green":
            if symbol == arcade.key.UP:
                self.player.change_y = -5

            if symbol == arcade.key.DOWN:
                self.player.change_y = 5

    def on_key_release_a(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released for player 1

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
        """Undo movement vectors when movement keys are released for player 2

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """

        if (
            symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0
