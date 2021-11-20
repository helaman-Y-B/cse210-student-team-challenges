import arcade
from game.constants import SCALING


class Players():
    """This class will make the players of our game.

    Sterio Type:
        game setup

    Attributes:
        """

    def player_maker(self, height, img_path, player_place):
        """This function will make the players."""
        self.player = arcade.Sprite(img_path, SCALING)
        self.player.center_y = height / 2
        self.player.left = player_place

        return self.player
