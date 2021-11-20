import arcade


class Update():

    def __init__(self, all_sprites):
        self.player = all_sprites

    def update(self, delta_time: float):
        # Update everything
        """for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )"""

        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

        # if self.player2.top > self.height:
        #    self.player2.top = self.height
        # if self.player2.right > self.width:
        #    self.player2.right = self.width
        # if self.player2.bottom < 0:
        #    self.player2.bottom = 0
        # if self.player2.left < 0:
        #    self.player2.left = 0
