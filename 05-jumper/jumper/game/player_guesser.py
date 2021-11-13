class Player_guesser:
    def __init__(self) -> None:
        self.answer = True

    def question(self):
        user_answer = "path to the user guess"

        if user_answer == int:
            print("The number was entered...\nPlease type a latter this time.")

        elif user_answer == str:
            alphabet = [
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]
            if user_answer in alphabet:
                self.answer = True

            elif user_answer in random_word:
                self.answer = False
