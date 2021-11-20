import arcade
from game.key_handler import KeyHandler
from game.on_draw import Draws
from game.update import Update
from game.players import Players


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
        KeyHandler(self.player1).on_key_press_a(
            symbol, modifiers)
        KeyHandler(self.player2).on_key_press_b(
            symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        KeyHandler(self.player1).on_key_release_a(
            symbol, modifiers)
        KeyHandler(self.player2).on_key_release_b(
            symbol, modifiers)

    def on_update(self, delta_time: float):
        """for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )"""
        # Update everything
        self.all_sprites.update()

        # Keep the player on screen
        Update(self.all_sprites, self.height).update(delta_time)
        self.draw()

    def draw(self):
        Draws(self.all_sprites).on_draw()
