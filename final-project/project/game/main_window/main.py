import arcade
from mainmenuwindow import MainMenuView

def main():
    """ Main function """

    window = arcade.Window(800, 600, "Menu")
    start_view = MainMenuView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()