import arcade
from constants import SCALING


class Players():
    """This class will make the players of our game.

    Sterio Type:
        game setup

    Attributes:
        """

    def player_maker(self, height, img_path):
        """This function will make the player."""
        if img_path == "img/player1_plataform.png":
            self.player = arcade.Sprite(img_path, SCALING)
            self.player.center_y = height / 2
            self.player.left = 100
        else:
            self.player = arcade.Sprite(img_path, SCALING)
            self.player.center_y = height / 2
            self.player.left = 715

        return self.player
