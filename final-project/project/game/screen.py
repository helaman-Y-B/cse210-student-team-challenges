import arcade
import random
from game.key_handler import KeyHandler
from game.on_draw import Draws
from game.update import Update
from game.players import Players
from game.box_draw import BoxDrawer
from game.score import Score


class PongGame(arcade.View):
    """Pong game is a game with to players
    where they try to get the ball reaches
    the enemy side so that they can make points.

    Sterio Type:
        Visual Game.

    Attributes:
        self.players: a SpriteList() for the two players.
        self.ball: a SpriteList() for the game ball.
        self.wall_list: a SpriteList() for the walls.
        self.limits_list: a SpriteList() for the limits of the game screen for objects.
        self.all_sprites: a SpriteList() for all the sprites (players and ball).
        self._players: the Players() class.
        self.output: a string.
        self.collided: a boolean value.
        self.score_p1: a interger value.
        self.score_p1: a interger value."""

    def __init__(self, width: int, height: int, title: str):
        """The constructor class, which
        makes the screen game to appear."""

        super().__init__()

        # Set up the empty Sprites.
        self.players = arcade.SpriteList()
        self.ball = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.limit_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self._players = Players()

        self.height = height
        self.width = width
        self.title = title

        self.output = ""
        self.collided = False
        self.score_p1 = 0
        self.score_p2 = 0

    def setup(self):
        """Sets the background color, the players,
        and ball.

        In the future it will be used for power ups and
        sounds/musics."""

        # Setup the backgound color
        arcade.set_background_color(arcade.color.GRAY)

        self.player1 = self._players.player_maker(
            self.height, "game/img/player1_plataform.png", 10)
        self.player2 = self._players.player_maker(
            self.height, "game/img/player2_plataform.png", 715)

        self.all_sprites.append(self.player1)
        self.all_sprites.append(self.player2)

        # self.all_sprites.append(self.score)

        # Create horizontal rows of boxes
        for x in range(0, self.width):
            # Bottom edge
            self.wall_list.append(BoxDrawer.box_drawer(
                x, self.height, self.width, "xbottom"))

            # Top edge
            self.wall_list.append(BoxDrawer.box_drawer(
                x, self.height, self.width, "xtop"))

        for y in range(0, self.height):
            # Bottom edge
            self.limit_list.append(BoxDrawer.box_drawer(
                y, self.height, self.width, "ybottom"))

            # Top edge
            self.limit_list.append(BoxDrawer.box_drawer(
                y, self.height, self.width, "ytop"))

        # Create ball
        ball = arcade.Sprite("game/img/ball.png", 0.25)
        ball.center_x = random.randrange(100, 700)
        ball.center_y = random.randrange(100, 500)
        while ball.change_x == 0 and ball.change_y == 0:
            ball.change_x = random.randrange(-4, 5)
            ball.change_y = random.randrange(-4, 5)

        self.all_sprites.append(ball)

        for i in self.wall_list:
            self.all_sprites.append(i)
        self.players.append(self.player1)
        self.players.append(self.player2)
        self.ball.append(ball)

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

        # This part is responsible for detecting when a player gets a point
        limits_hit = arcade.check_for_collision_with_list(
            self.all_sprites[2], self.limit_list)

        for limit in limits_hit:
            if self.all_sprites[2].change_x > 0:
                self.all_sprites[2].center_x = random.randrange(200, 700)
                self.all_sprites[2].center_y = random.randrange(200, 500)
                self.all_sprites[2].top = limit.bottom

            elif self.all_sprites[2].change_x < 0:
                self.all_sprites[2].center_x = random.randrange(400, 500)
                self.all_sprites[2].center_y = random.randrange(200, 500)
                self.all_sprites[2].bottom = limit.top

        x_position = self.all_sprites[2]._get_center_x()
        print(f"Coordinates: {x_position}")

        if len(limits_hit) > 0:
            self.all_sprites[2].change_x *= -1

        if x_position >= 740:
            self.score_p1 += 1
            print("After p1 points")

        elif x_position <= 54:
            self.score_p2 += 1
            print("After p2 points")

        # Keep the player on screen
        Update(self.all_sprites, self.wall_list, self.players, self.limit_list,
               self.height).update(delta_time)

        self.draw()

    def draw(self):
        """Draws all the information unto the screen."""
        Draws(self.all_sprites, self.output).on_draw()
        Score.draw_score(self)
