from game.constants import MAX_X, MAX_Y
from game.point import Point
from game.word_provider import WordProvider


class OutputService:
    """The OutputService send the word that the user needs to type.

    Stereotype:
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen."""

    def __init__(self, screen):
        """The class constructor.

        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        self.__list_words = []
        self._screen = screen
        self.point = Point()
        self.word = WordProvider()

    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * MAX_X, 0, 0, 7)
        self._screen.print_at("-" * MAX_X, 0, MAX_Y, 7)

    def draw_interface(self, interface):
        text1, x1, y1 = interface.get_score()

        text2, x2, y2 = interface.get_buffer()

        self._screen.print_at(text1, x1, y1, 7)
        self._screen.print_at(text2, x2, y2, 7)

    def draw_word(self):
        self.__list_words = []
        while len(self.__list_words) < 5:
            for j in self.word.update_words():
                word = j[0]
                x = j[1]
                y = j[2]
                self._screen.print_at(word, x, y, 7)
                self.__list_words.append(word)
            break

    def get_words(self):
        return self.__list_words

    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self._screen.refresh()
