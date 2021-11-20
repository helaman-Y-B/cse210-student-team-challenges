import arcade


class Update():

    def __init__(self, all_sprites, height):
        self.player = all_sprites
        self.height = height

    def update(self, delta_time: float):
        """for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )"""

        # Keep the player on screen
        if self.player[0].top > self.height:
            self.player[0].top = self.height
        if self.player[1].top > self.height:
            self.player[1].top = self.height
        if self.player[0].bottom < 0:
            self.player[0].bottom = 0
        if self.player[1].bottom < 0:
            self.player[1].bottom = 0
