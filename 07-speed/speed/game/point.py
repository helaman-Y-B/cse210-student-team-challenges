import random
from game.constants import MAX_X, MAX_Y


class Point:
    """Represents distance from an origin (0, 0).

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance.
        _y (Point): The vertical distance.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Point): An instance of Point.
            x (integer): A horizontal distance.
            y (integer): A vertical distance.
        """
        self._x = random.randrange(MAX_X+1)
        self._y = random.randrange(MAX_Y+1)

    def new_coordinates(self):
        points = self._x, self._y
        return points

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            self (Point): An instance of Point.
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            self (Point): An instance of Point.
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.

        Args:
            self (Point): An instance of Point.

        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_new_x(self):
        """Gets the horizontal distance.

        Args:
            self (Point): An instance of Point.

        Returns:
            integer: The horizontal distance.
        """
        x = random.randrange(1, MAX_X)

        return x

    def get_new_y(self):
        """Gets the horizontal distance.

        Args:
            self (Point): An instance of Point.

        Returns:
            integer: The horizontal distance.
        """
        y = random.randrange(1, MAX_Y)

        return y

    def move(self, words):

        direction = "n", "s", "e", "w", "ne", "se", "sw", "nw"
        new_position = []

        for i in words:
            word, x, y = i
            var1 = direction[random.randrange(len(direction))]
            if "n" == var1:
                data = word, x, y+1
                new_position.append(data)
            elif "s" == var1:
                data = word, x, y-1
                new_position.append(data)
            elif "e" == var1:
                data = word, x-1, y
                new_position.append(data)
            elif "w" == var1:
                data = word, x+1, y
                new_position.append(data)
            elif "ne" == var1:
                data = word, x+1, y+1
                new_position.append(data)
            elif "se" == var1:
                data = word, x+1, y-1
                new_position.append(data)
            elif "sw" == var1:
                data = word, x-1, y-1
                new_position.append(data)
            elif "nw" == var1:
                data = word, x-1, y+1
                new_position.append(data)

        return new_position

    def get_y(self):
        """Gets the vertical distance.

        Args:
            self (Point): An instance of Point.

        Returns:
            integer: The vertical distance.
        """
        return self._y

    def reverse(self):
        """Gets a new Point that is the reverse of this one.

        Args:
            self (Point): An instance of Point.

        Returns:
            Point: A new Point that is reversed.
        """
        x = self._x * -1
        y = self._y * -1
        return Point(x, y)
