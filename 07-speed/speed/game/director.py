# ~ from game.input_service import InputService
from game.word_provider import WordProvider
from game.interface import Interface
from game.user_validation import Validation
from time import sleep


class Director:
    """The Director class directs the data to each class from the game in an order,
    so that the game can continue.

    Stereotype:
        Controller

    Attributes:
        _word: The word that the user needs to type."""

    def __init__(self, input_service, output_service):
        self._word = WordProvider()
        self._keep_playing = True
        self._output_service = output_service
        self._input_service = input_service
        self._interface = Interface()
        self.__validation = Validation()

    def start_game(self):
        while self._keep_playing:
            self._get_input()
            self._get_outputs()
            sleep(1.0)

    def _get_input(self):
        letter = self._input_service.get_letter()
        self.__validation._guessed_word(letter)
        self._interface.set_buffer(letter, self._output_service.get_words())
        self._interface.get_buffer()

    def _get_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_interface(self._interface)
        self._output_service.draw_word()
        self._output_service.flush_buffer()
