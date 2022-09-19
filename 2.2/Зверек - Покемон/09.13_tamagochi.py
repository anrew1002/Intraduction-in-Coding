from datetime import datetime as dt
from pickletools import StackObject


class State:
    Angry = 0
    Sad = 1
    Normal = 2
    Kind = 3
    Happy = 4
    Cheerful = 5
    Dead = 6


class tamagochi:
    def __init__(self, name="Anon", eat_timeout=10):
        self.__name = name
        self.__eat_timeout = eat_timeout
        self.__st = dt.now()
        self.__state = State.Normal
        
