import arcade
import pathlib
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


class WinnerView(arcade.View):
    """This class will display main menu screen to the player"""

    def __init__(self, player_num):
        super().__init__()
        self.player_number = player_num

    def on_show(self):
        """draw everthing"""

        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        game_banner = arcade.load_texture(pathlib.Path(
            __file__).parent / "winner_img/winner.png")

        arcade.draw_texture_rectangle(
            self.window.width / 2, self.window.height / 2, 600, 200, game_banner)

        winner_player = f"PLAYER {self.player_number} WINS"

        arcade.draw_text(winner_player, self.window.width / 2,
                         400, arcade.color.YELLOW, font_size=50, font_name="Kenney Blocks", anchor_x="center")

        instruction = "Press [M] to go close the window"

        arcade.draw_text(instruction, self.window.width / 2,
                         150, arcade.color.YELLOW, font_size=30, font_name="Kenney Future", anchor_x="center",  multiline=True, width=500, align="center")

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.M:
            print("Game Ended")
            arcade.close_window()
            # Create a new Pong Game window

    def setup(self):

        winner_music = arcade.load_sound(pathlib.Path(
            __file__).parent / "sounds/mixkit-game-level-completed-2059.wav")
        #print("sound start")
        arcade.play_sound(winner_music)
        #print("sound end")
