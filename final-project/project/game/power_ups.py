import arcade
import pathlib


class PowerUps():
    def __init__(self) -> None:
        self.power_up = 0

    def draw_power(self, img_path):
        self.power = arcade.Sprite(pathlib.Path(
            __file__).parent / img_path, 0.25)
        self.power.center_x = 1000
        self.power.center_y = 1000

        return self.power
