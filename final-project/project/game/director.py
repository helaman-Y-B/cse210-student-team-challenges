from project.game.screen import PongGame
from project.game.constants import SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, SCALING


class Director():

    def __init__(self):
        self.screen = PongGame(int(SCREEN_WIDTH * SCALING),
                               int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE)
