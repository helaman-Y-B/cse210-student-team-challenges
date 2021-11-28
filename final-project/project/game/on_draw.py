import arcade
#from game.score import ScoreS


class Draws():
    """Draw all game objects"""

    def __init__(self, all_sprites, text):
        self.all_sprites = all_sprites
        self.output = text

    def on_draw(self):
        # Draw all the sprites.
        arcade.start_render()
        # Score.draw_score(self)
        self.all_sprites.draw()

        arcade.draw_text(self.output, 10, 10)
