from game.constants import LIBRARY
from game.point import Point
from game.constants import MAX_X, MAX_Y
import random


class WordProvider:
    """The Class WordProvider, provides a random word from a list of words.

    Stereotype:
        Gameplay.

    Attributes:
        _word (Word): An Random word from a list."""

    def __init__(self):

        self.point = Point()

        self._word1 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()
        self._word2 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()
        self._word3 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()
        self._word4 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()
        self._word5 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()

        self._word_state = True
        self._word = ""
        self._list_of_words = []

    def update_words(self):
        if self._word_state:
            self._word1 = f"{self.get_words()[0]}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._word2 = f"{self.get_words()[1]}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._word3 = f"{self.get_words()[2]}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._word4 = f"{self.get_words()[3]}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._word5 = f"{self.get_words()[4]}", self.point.get_new_x(
            ), self.point.get_new_y()

        words = self._word1, self._word2, self._word3, self._word4, self._word5

        return words

    def word_picker(self):
        self._word = random.choice(LIBRARY)
        return self._word

    def get_words(self):
        words = self._word1[0], self._word2[0], self._word3[0], self._word4[0], self._word5[0]
        return words
