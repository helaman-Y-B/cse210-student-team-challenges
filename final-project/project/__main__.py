import arcade
from game.screen import PongGame
from game.on_draw import Draws
from game.constants import SCALING, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE
from game.update import Update


def main():
    # Create a new Pong Game window
    pong_game = PongGame(int(SCREEN_WIDTH * SCALING),
                         int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE)
    # Run the game
    arcade.run()


if __name__ == "__main__":
    main()
