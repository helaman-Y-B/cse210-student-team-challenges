from game.constants import MAX_X, MAX_Y
from game.score import Score


class Interface:
    """A part of the interface, it prints current score and buffer words entered by the user
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Interface): an instance of Interface.
        """
        self._text1 = "Score: "
        self._text2 = "Buffer: "
        self._score = Score()
        self._buffer = ""

    def get_score(self):
        """Gets current score.

        Args:
            self (Interface): an instance of Interface.

        Returns:
            String: A string concatenated self._text1 + self._score
        """
        text = f"{self._text1}{self._score._show_current_score()}", 0, 0
        return text

    def get_buffer(self):
        """Gets current buffer.

        Args:
            self (Interface): an instance of Interface.

        Returns:
            String: A string concatenated self._text2 + self._buffer
        """
        text = f"{self._text2}{self._buffer}", 0, MAX_Y
        return text

    def set_buffer(self, letter, words):
        if self._buffer in words:
            self._score.increase_score()
            self._buffer = ""
        if len(letter) > 0:
            self._buffer = self._buffer + letter
        if "*" in letter:
            self._buffer = ""
