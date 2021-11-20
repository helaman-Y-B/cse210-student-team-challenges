import arcade
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

        self.setup()

    def setup(self):
        """Sets the background color, the players,
        and ball.

        In the future it will be used for power ups and
        sounds/musics."""

        # Setup the backgound color
        arcade.set_background_color(arcade.color.BLACK)

        # Setup the players
        # self.player1 = Players().player_maker(
        #    self.height, "project/game/img/player1_plataform.png")
        # self.all_sprites.append(self.player1)
        # self.player2 = Players().player_maker(
        #    self.height, "project/game/img/player2_plataform.png")
        # self.all_sprites.append(self.player2)

        # Set up the player
        self.player1 = arcade.Sprite(
            "project/game/img/player1_plataform.png", SCALING)
        self.player1.center_y = self.height / 2
        self.player1.left = 10
        self.all_sprites.append(self.player1)

        self.player2 = arcade.Sprite(
            "project/game/img/player2_plataform.png", SCALING)
        self.player2.center_y = self.height / 2
        self.player2.left = 715
        self.all_sprites.append(self.player2)
        # return self.all_sprites

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player1.change_y = 5

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player1.change_y = -5

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.I
            or symbol == arcade.key.K
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player1.change_y = 0

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
        if self.player1.top > self.height:
            self.player1.top = self.height
        if self.player1.right > self.width:
            self.player1.right = self.width
        if self.player1.bottom < 0:
            self.player1.bottom = 0
        if self.player1.left < 0:
            self.player1.left = 0

        if self.player2.top > self.height:
            self.player2.top = self.height
        if self.player2.right > self.width:
            self.player2.right = self.width
        if self.player2.bottom < 0:
            self.player2.bottom = 0
        if self.player2.left < 0:
            self.player2.left = 0

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()


if __name__ == "__main__":
    app = PongGame(SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_TITLE)
    arcade.run()
