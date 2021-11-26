import arcade
from game.score import Score


class Draws():
    """Draw all game objects"""

    def __init__(self, all_sprites, text, score):
        self.all_sprites = all_sprites
        self.output = text
        self.score = score

    def on_draw(self):
        # Draw all the sprites.
        arcade.start_render()
        Score(self.score).draw_score()
        self.all_sprites.draw()

        arcade.draw_text(self.output, 10, 10)
