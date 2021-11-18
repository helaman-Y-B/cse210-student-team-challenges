import arcade
from arcade import sprite


class Draws():
    """Draw all game objects"""

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()
