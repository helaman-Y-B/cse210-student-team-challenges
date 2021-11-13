from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        event_type, direction = self._input_service.get_direction()
        
        if direction:
            paddle = cast["paddle"][0]
            new_position = paddle.get_position().add(direction)
            if -1 < new_position.get_x() < constants.MAX_X - 10:
                paddle.set_position(new_position)        
