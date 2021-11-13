from time import sleep
from game import constants
from game.output_service import OutputService
from game.interface import Interface


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller
    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script, screen, points):
        """The class constructor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._points = points
        self._output_service = OutputService(screen, points)
        self._interface = Interface(self._points)

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.

        Args:
            tag (string): The given tag.
        """

        for action in self._script[tag]:
            self._points -= 1
            action.execute(self._cast)
