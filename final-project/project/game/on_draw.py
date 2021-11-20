import arcade


class Draws():
    """Draw all game objects"""

    def __init__(self, all_sprites) -> None:
        self.all_sprites = all_sprites

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()
