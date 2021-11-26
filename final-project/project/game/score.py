import arcade
from game.constants import SCREEN_WIDTH
from game.update import Update


class Score():
    def __init__(self, score):
        self.score = score

        #self.score_for_p1 = Update.send_current_score(self.score_player1)
        #self.score_for_p2 = Update.send_current_score(self.score_player2)

    def draw_score(self):
        arcade.draw_text(str(self.score), SCREEN_WIDTH/2 - 50, 500,
                         arcade.color.YELLOW, 30, 200, "left")

        arcade.draw_text(str(self.score), SCREEN_WIDTH/2 - 100, 500,
                         arcade.color.YELLOW, 30, 200, "right")
