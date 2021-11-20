from game.players import Players
from game.screen import PongGame


class Update(Players, PongGame):

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
