from game.lives import Lives
# ~ will accept rambom words
# ~ will hide it from the player
# ~ will evaluate the player entry letter if is true to the ramdom words
# print guess a letter

class Puzzle:
    
    def __init__(self):
        """Initialize 
        """
        self.parachute_man = ["", "  ___", " /___\ ", " \   /", "  \ /", "   0", "  /|\ ", "  / \ ", "", "^^^^^^^", ""]
        self.intents = 4
        self.dead_man = ["", "   X", "  /|\ ", "  / \ ", "", "^^^^^^^", ""]
        self.letters = []
        self.progress = 0
        

            
    def set_word(self, word):
        """Sets the word to initialize the game interface.
        Args:
            word: the word chosen randomly.
        """
        self.word = word
        self.word_interface = ""
        
        for _ in word:
            self.word_interface += "_ "

    def interface(self, lives):
        """It generates the game interface.
        Args:
            score: current score.
        """
        # ~ print(len(self.parachute_man))
        
        # ~ if self.intents < lives:
            # ~ self.parachute_man.pop(1)
    
        data = [self.word_interface, ]
        
        for i in self.parachute_man:
            data.append(i)
        
        if len(self.parachute_man) == 7:
            return self.dead_man
        else:
            return data

        
        
    def question(self):
        """It returns the game's question.
        """
        main_question = "Guess a letter [a-z]: "
        
        return main_question
        
    def evaluate(self, letter):
        """It compares the current letter with the word and sets the new interface.
        Args:
            letter: current score.
        """
        if letter in self.word and letter not in self.letters:
            
            cur_index = []
            counter = 0
            for i in list(self.word):
                if letter in i:
                    cur_index.append(counter)
                counter +=1
            # ~ print(f" letters founded {cur_index}")
             
            
                
            # ~ lister = list(self.word_interface)
            for i in cur_index:
                lister = list(self.word_interface)
                index = i * 2
                lister[index] = letter
                self.word_interface = "".join(lister)
                self.letters.append(letter)
                self.progress += 1
            return True
        else:
            self.intents -= 1
            self.parachute_man.pop(1)
            # ~ print("descontando 1")
            return False
        
    def dead_man(self):
        """Returns self.dead_man when the game ends
        
        """
        
        return self.dead_man
        
    def survivor_man(self):
        survivor = "Congratulations, you survived!"
        return survivor
            
        
            
            
            
            
