import arcade
from key_handler import KeyHandler
from update import Update
from players import Players
from constants import SCREEN_HEIGHT, SCALING, SCREEN_TITLE, SCREEN_WIDTH
#from on_draw import Draws


class PongGame(arcade.Window):
    """Pong game is a game with to players
    where they try to get the ball reaches
    the enemy side so that they can make points.

    Sterio Type:
        Visual Game.

    Attributes:
        self.players: a SpriteList() for the two players.
        self.ball: a SpriteList() for the game ball.
        self.all_sprites: a SpriteList() for all the sprites (players and ball)"""

    def __init__(self, width: int, height: int, title: str):
        """The constructor class, which
        makes the screen game to appear."""

        super().__init__(width, height, title)

        # Set up the empty Sprites.
        self.players = arcade.SpriteList()
        self.ball = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self._players = Players()

        self.setup()

    def setup(self):
        """Sets the background color, the players,
        and ball.

        In the future it will be used for power ups and
        sounds/musics."""

        # Setup the backgound color
        arcade.set_background_color(arcade.color.BLACK)

        self.player1 = self._players.player_maker(
            self.height, "game/img/player1_plataform.png", 10)
        self.player2 = self._players.player_maker(
            self.height, "game/img/player2_plataform.png", 715)

        self.all_sprites.append(self.player1)
        self.all_sprites.append(self.player2)

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/K: Move Up, Down
        Arrows: Move Up, Down

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W:
            self.player1.change_y = 5

        if symbol == arcade.key.UP:
            self.player2.change_y = 5

        if symbol == arcade.key.S:
            self.player1.change_y = -5

        if symbol == arcade.key.DOWN:
            self.player2.change_y = -5

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player1.change_y = 0
        if (
            symbol == arcade.key.W
            or symbol == arcade.key.S
        ):
            self.player2.change_y = 0

    def on_update(self, delta_time: float):
        # Update everything
        self.all_sprites.update()
        """for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )"""

        # Keep the player on screen
        Update(self.all_sprites)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()


if __name__ == "__main__":
    app = PongGame(SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_TITLE)
    arcade.run()
