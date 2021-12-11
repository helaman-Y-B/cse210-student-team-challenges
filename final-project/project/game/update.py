import arcade
import random


class Update():

    def __init__(self, all_sprites, wall_list, players_list, limit_list, power_ups, height):
        self.sprite = all_sprites
        self.height = height
        self.wall_list = wall_list
        self.players_list = players_list
        self.limit_list = limit_list
        self.power_up_list = power_ups

    def update(self, delta_time: float):
        """for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )"""

        # Keep the player on screen
        if self.sprite[0].top > self.height:
            self.sprite[0].top = self.height
        if self.sprite[1].top > self.height:
            self.sprite[1].top = self.height
        if self.sprite[0].bottom < 0:
            self.sprite[0].bottom = 0
        if self.sprite[1].bottom < 0:
            self.sprite[1].bottom = 0

        # This part of code will close the screen if there is no bottom or top wall hit

        # Check colision of the ball with the players
        player_hit = arcade.check_for_collision_with_list(
            self.sprite[2], self.players_list)

        for player in player_hit:

            if self.sprite[2].change_x > 0:
                self.sprite[2].right = player.left
                self.sprite[2].change_x = random.randrange(5, 10)
                self.sprite[2].change_y = random.randrange(-5, 5)
            elif self.sprite[2].change_x < 0:
                self.sprite[2].left = player.right
                self.sprite[2].change_x = random.randrange(-10, -5)
                self.sprite[2].change_y = random.randrange(-5, 5)

        if len(player_hit) > 0:
            self.sprite[2].change_x *= -1

        # Check colision of the ball with the walls
        self.sprite[2].center_y += self.sprite[2].change_y

        walls_hit = arcade.check_for_collision_with_list(
            self.sprite[2], self.wall_list)

        for wall in walls_hit:

            if self.sprite[2].change_y > 0:
                self.sprite[2].top = wall.bottom

            elif self.sprite[2].change_y < 0:
                self.sprite[2].bottom = wall.top

        if len(walls_hit) > 0:
            self.sprite[2].change_y *= -1

        # Check colision of the player with the ball
        player_hit = arcade.check_for_collision_with_list(
            self.sprite[2], self.players_list)
        for player in player_hit:
            if self.sprite[2].change_y > 0:

                self.sprite[2].top = player.bottom
            if self.sprite[2].change_y < 0:
                self.sprite[2].bottom = player.top
        if len(player_hit) > 0:
            self.sprite[2].change_y *= -1

        # Check colision of the player with the wall
        player_inter = arcade.check_for_collision_with_list(
            self.sprite[0], self.wall_list)
        if len(player_inter) > 0:
            self.sprite[0].change_x *= -1

        # Handles power ups collisions.
        if self.sprite[2].collides_with_list(self.power_up_list):

            # Handles the red power up
            # The red orb gets the player closer to the center
            if self.sprite[2].collides_with_sprite(self.power_up_list[0]):

                self.power_up_list[0].center_x = 1000

                print("Let's get closer!!")
                return "red"

            # Handles the green power up
            # Invert controls of both players
            elif self.sprite[2].collides_with_sprite(self.power_up_list[1]):

                self.power_up_list[1].center_x = 1000

                print("Oh no!! We are upside down!")
                return "green"

            # Handles the blue power up
            # Inverts the players sides
            elif self.sprite[2].collides_with_sprite(self.power_up_list[2]):

                self.power_up_list[2].center_x = 1000

                print("Let's change sides!!")
                return "blue"

            # Handles the yellow power up
            # Make the paddles velocities
            elif self.sprite[2].collides_with_sprite(self.power_up_list[3]):

                self.power_up_list[3].center_x = 1000

                print("Everybody is Slower!!")
                return "yellow"

    def update_score(self):
        self.score += 1
        return self.score
