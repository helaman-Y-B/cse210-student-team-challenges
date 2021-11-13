import sys
from asciimatics.event import KeyboardEvent


class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.

        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen

    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = self._screen.get_key()
        if not event is None:
            if event == 40:
                sys.exit()
            elif event == 10 or event == 13:
                result = "*"
            elif event >= 97 and event <= 122:
                result = chr(event)
        return result
