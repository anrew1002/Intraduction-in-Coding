from datetime import datetime as dt


class State:
    Angry = 0
    Sad = 1
    Normal = 2
    Kind = 3
    Happy = 4
    Cheerful = 5
    Dead = 6

class Xrxr:
    # states = {"Angry": 1, "Sad": 2, "Normal": 3, "Daed": 4, "Kind": 5, "Happy": 6, "Cheerful": 7}

    def __init__(self, name="Anon", eat_timeout=10):
        self.__name = name
        self.__eat_timeout = eat_timeout
        self.__st = dt.now()
        self.__state = Xrxr.states["Normal"]

    def eat(self, amount=0):
        """Покормить"""
        if amount == 0:
            self.__state = State.Angry
            return
        st.diff = (dt.now() - st).seconds()
        if st.diff > 30:
            self.__state =State.Dead
            return
        if st.diff > 20:
            if amount - 2 < 0:
                self.__state = State.Angry
                st = dt.now()
            else:
                self.__state = State.Normal
                st = dt.now()

            return

        if amount == 1:
            self.__state = Xrxr.states["Sad"]
        if amount == 2:
            self.__state = Xrxr.states[""]

    def state(self):
        if (dt.now() - st).seconds() > 30:
            self.__state = Xrxr.states["Dead"]
        return self.__state

    # @property
    # def state(self):
    #     return self.__state
    #
    # @state.setter
    # def state(self):
    #     self.__state = state


a = Xrxr()
