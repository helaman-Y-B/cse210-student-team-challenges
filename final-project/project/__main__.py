import arcade
from game.screen import PongGame
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE


def main():
    # Create a new Pong Game window
    PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # Run the game again
    arcade.run()


if __name__ == "__main__":
    main()
