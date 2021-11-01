import os

MAX_X = 800
MAX_Y = 400
FRAME_RATE = 30

DEFAULT_SQUARE_LENGTH = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 5

MAX_SPEED = 5
WORD_GENERATION_RATE = 0.02

STARTING_WORDS = 5
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()

