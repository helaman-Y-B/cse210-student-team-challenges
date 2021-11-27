import arcade
from game.constants import SCREEN_WIDTH


class Score():
    """The Score class is responsible to show the score into the game screen.

    Sterio Type:
        Visual Game.
        """

    def draw_score(self):
        arcade.draw_text(str(self.score_p1), SCREEN_WIDTH/2 - 50, 500,
                         arcade.color.YELLOW, 30, 200, "left")

        arcade.draw_text(str(self.score_p2), SCREEN_WIDTH/2 - 100, 500,
                         arcade.color.YELLOW, 30, 200, "right")
