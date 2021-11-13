from game.constants import MAX_X, MAX_Y
from game.score import Score


class Interface:
    """A part of the interface, it prints current score and buffer words entered by the user
    """

    def __init__(self, points):
        """The class constructor.

        Args:
            self (Interface): an instance of Interface.
        """
        self._text1 = "Score: "
        self._score = Score(points)

    def get_score(self):
        """Gets current score.

        Args:
            self (Interface): an instance of Interface.

        Returns:
            String: A string concatenated self._text1 + self._score
        """
        text = f"{self._text1}{self._score._show_current_score()}" * 1, 0, 0,
        return text
