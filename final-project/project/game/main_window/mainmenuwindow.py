import arcade
import pathlib
from game.screen import PongGame
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


class MainMenuView(arcade.View):
    """This class will display main menu screen to the player"""

    def on_show(self):
        """draw everthing"""

        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

        arcade.set_viewport(0, self.window.width, 0, self.window.height)

        background_music = arcade.load_sound(pathlib.Path(
            __file__).parent / "music/silly_creature_130_proud_music_preview.mp3")
        print("sound start")
        arcade.play_sound(background_music)
        print("sound end")

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        game_banner = arcade.load_texture(
            pathlib.Path(__file__).parent / "menu_img/pong.jpg")

        arcade.draw_texture_rectangle(
            self.window.width / 2, self.window.height - 100, 600, 200, game_banner)

        arcade.draw_text("WELCOME TO PONG", self.window.width / 2,
                         350, arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text("INSTRUCTIONS:", self.window.width / 2, self.window.height /
                         2, arcade.color.WHITE, font_size=20, anchor_x="center")

        instructions = "Pong is a two-dimensional sports game that simulates table tennis. The player controls an in-game paddle by moving it vertically across the left or right side of the screen. They can compete against another player controlling a second paddle on the opposing side. Players use the paddles to hit a ball back and forth."

        arcade.draw_text(instructions, self.window.width / 2, self.window.height / 2-20, arcade.color.WHITE,
                         font_size=14, anchor_x="center", multiline=True, width=600, align="center")

        arcade.draw_text("Player 1 Control", 200, self.window.height /
                         2-150, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("[ W ] = Move Up", 200, self.window.height / 2-175,
                         arcade.color.WHITE, font_size=14, anchor_x="center", align="left")
        arcade.draw_text("[ S ] = Move Down", 200, self.window.height / 2-195,
                         arcade.color.WHITE, font_size=14, anchor_x="center", align="left")

        arcade.draw_text("Player 2 Control", 600, self.window.height /
                         2-150, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("[ ↑ ] = Move Up", 600, self.window.height / 2-175,
                         arcade.color.WHITE, font_size=14, anchor_x="center", align="left")
        arcade.draw_text("[ ↓ ] = Move Down", 600, self.window.height / 2-195,
                         arcade.color.WHITE, font_size=14, anchor_x="center", align="left")

        arcade.draw_text("[ P ] = Re-Position the ball", self.window.width / 2, self.window.height / 2-225,
                         arcade.color.WHITE, font_size=14, anchor_x="center", align="left")

        arcade.draw_text("Press [S] to Start Game and [Q] to end!", self.window.width / 2,
                         self.window.height / 2 - 250, arcade.color.RED, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.S:
            print("Will start the game")
            game_view = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
            # Create a new Pong Game window
            game_view.setup()

            self.window.show_view(game_view)
        elif symbol == arcade.key.Q:
            arcade.close_window()
