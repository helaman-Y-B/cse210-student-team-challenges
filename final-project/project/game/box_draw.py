import arcade


class BoxDrawer():

    def box_drawer(direction, height, width, command):
        if command == "xbottom":
            # Bottom edge
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", 0.5)
            wall.center_x = direction
            wall.center_y = 0
            return wall

        elif command == "xtop":
            # Top edge
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", 0.5)
            wall.center_x = direction
            wall.center_y = height

            return wall

        elif command == "ybottom":
            limits = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", 0.5)
            limits.center_x = 0
            limits.center_y = direction

            return limits

        elif command == "ytop":
            # Top edge
            limits = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", 0.5)
            limits.center_x = width-10
            limits.center_y = direction

            return limits
