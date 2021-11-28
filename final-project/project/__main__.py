import arcade
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.main_window.mainmenuwindow import MainMenuView


def main():

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")
    start_view = MainMenuView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
