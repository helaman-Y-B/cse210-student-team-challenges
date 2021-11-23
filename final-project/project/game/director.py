from game.key_handler import KeyHandler
from game.players import Players
from game.screen import PongGame
from game.constants import SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, SCALING


class Director(PongGame):

    def __init__(self):

        super().__init__(SCREEN_WIDTH * SCALING, SCREEN_HEIGHT * SCALING, SCREEN_TITLE)
        self._players = Players()

    def call_functions(self):
        KeyHandler()
