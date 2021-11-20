import arcade


class Update():

    def __init__(self, all_sprites, wall_list,  height):
        self.sprite = all_sprites
        self.height = height
        self.wall_list = wall_list

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
        # if not(self.wall_hit_collided):
        #     arcade.close_window()

        # for self.sprite[2]:

        self.sprite[2].center_x += self.sprite[2].change_x
        walls_hit = arcade.check_for_collision_with_list(
            self.sprite[2], self.wall_list)
        for wall in walls_hit:
            if self.sprite[2].change_x > 0:
                self.sprite[2].right = wall.left
            elif self.sprite[2].change_x < 0:
                self.sprite[2].left = wall.right
        if len(walls_hit) > 0:
            self.sprite[2].change_x *= -1

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

        # the following line of code is not working as is
        # Did we hit bottom and top wall? If true continue
        # if self.sprite[2].collides_with_list(self.wall_list):
        #    self.collided = True
        # else:
        #    self.collided = False
