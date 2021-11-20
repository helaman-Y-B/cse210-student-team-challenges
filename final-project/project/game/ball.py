import arcade
import os
import random

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Bouncing balls"

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.

        # Sprite lists
        self.ball_list = None
        self.wall_list = None
        self.output = ""
        self.collided = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.wall_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        # -- Set up the walls

        # Create horizontal rows of boxes
        for x in range(0, SCREEN_WIDTH):
            # Bottom edge
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

            # Top edge
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = SCREEN_HEIGHT
            self.wall_list.append(wall)

        # Create ball
        ball = arcade.Sprite("project/game/img/ball.png", 0.25)
        ball.center_x = random.randrange(100, 700)
        ball.center_y = random.randrange(100, 500)
        while ball.change_x == 0 and ball.change_y == 0:
            ball.change_x = random.randrange(-4, 5)
            ball.change_y = random.randrange(-4, 5)

        self.ball_list.append(ball)

        # Set the background color
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.ball_list.draw()
        arcade.draw_text(self.output, 10, 10)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # This part of code will close the screen if there is no bottom or top wall hit
        # if not(self.wall_hit_collided):
        #     arcade.close_window()

        for ball in self.ball_list:

            ball.center_x += ball.change_x
            walls_hit = arcade.check_for_collision_with_list(
                ball, self.wall_list)
            for wall in walls_hit:
                if ball.change_x > 0:
                    ball.right = wall.left
                elif ball.change_x < 0:
                    ball.left = wall.right
            if len(walls_hit) > 0:
                ball.change_x *= -1

            ball.center_y += ball.change_y
            walls_hit = arcade.check_for_collision_with_list(
                ball, self.wall_list)
            for wall in walls_hit:
                if ball.change_y > 0:
                    ball.top = wall.bottom
                elif ball.change_y < 0:
                    ball.bottom = wall.top
            if len(walls_hit) > 0:
                ball.change_y *= -1

        # the following line of code is not working as is
        # Did we hit bottom and top wall? If true continue
        if ball.collides_with_list(self.wall_list):
            self.collided = True
        else:
            self.collided = False


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
