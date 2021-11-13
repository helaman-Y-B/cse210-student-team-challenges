from game.word_provider import WordProvider


class Validation(WordProvider):
    def __init__(self):
        self._word_state = True
        self.__word_provider = WordProvider()
        self._word1 = f"{self.__word_provider.get_words()[0]}"
        self._word2 = f"{self.__word_provider.get_words()[1]}"
        self._word3 = f"{self.__word_provider.get_words()[2]}"
        self._word4 = f"{self.__word_provider.get_words()[3]}"
        self._word5 = f"{self.__word_provider.get_words()[4]}"

    def _guessed_word(self, user_string):
        if self._word1[0] == user_string:
            user_string = ""
        elif self._word2[0] == user_string:
            user_string = ""
        elif self._word3[0] == user_string:
            user_string = ""
        elif self._word4[0] == user_string:
            user_string = ""
        elif self._word5[0] == user_string:
            user_string = ""
