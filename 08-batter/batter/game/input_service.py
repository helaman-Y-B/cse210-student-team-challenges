import sys
from game.point import Point
from asciimatics.event import KeyboardEvent
from asciimatics.event import MouseEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[119] = Point(0, -1) # w
        self._keys[115] = Point(0, 1) # s
        self._keys[97] = Point(-4, 0) # a
        self._keys[100] = Point(4, 0) # d
        
    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        # direction = Point(0, 0)
        # event = self._screen.get_event()
        # if isinstance(event, KeyboardEvent):
        #     if event.key_code == 27:
        #         sys.exit()
        #     direction = self._keys.get(event.key_code, Point(0, 0))
        # return direction

        direction = None
        event_type = None
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            direction = self._keys.get(event.key_code)
            event_type = "keyboard"
        # if isinstance(event, MouseEvent):
            
        #     direction = Point(int(event.x), 0)
        #     event_type = "mouse"

        return event_type, direction
