import arcade
from winner_message import WinnerView

def main():
    """ Main function """

    window = arcade.Window(800, 600, "Menu")
    start_view = WinnerView("1")
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()