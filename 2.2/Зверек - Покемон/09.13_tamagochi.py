from datetime import datetime as dt


class State:
    Dead = -1
    Angry = 0
    Sad = 1
    Normal = 2
    Kind = 3
    Happy = 4
    Cheerful = 5
    # def update(self, count, original):


class Satisfaction:
    Disgruntled = 0
    Nice = 1
    Euphoria = 2


class tamagochi:

    def __init__(self, name="Anon", eat_timeout=5):
        self.__flag = True
        self.__name = name
        self.__eat_timeout = eat_timeout
        self.__st = dt.now()
        self.__state = State.Normal
        self.__satisfaction = Satisfaction.Nice

    def __str__(self):
        return str(f"Name: {self.__name}, Status:  {self.__state} (-1 to 5), Satisfaction:  {self.__satisfaction} (0 to 2)")

    def eat(self, count):
        if self.__state != State.Dead:
            self.__state += count
            self.__st = dt.now()
        if self.__state > State.Cheerful:
            self.__state = State.Cheerful

    def play(self):
        if self.__state != State.Dead:
            self.__satisfaction += 1
        if self.__state > Satisfaction.Euphoria:
            self.__satisfaction = Satisfaction.Euphoria

    def state_check(self):
        if self.__state == State.Dead:
            self.anigilation()
        elif (delta := ((dt.now()-self.__st).seconds)) >= self.__eat_timeout and self.__state != State.Dead:
            self.__state -= delta//self.__eat_timeout
            self.__st = dt.now()
            if self.__state < State.Dead:
                self.__state = State.Dead

    def anigilation(self):
        if self.__flag == True:
            self.__satisfaction = "in heaven with happiness"
            print(f"Зверь {self.__name} умер!")
            self.__flag = False


running = True
bestiary = {}
print("Приветствую!, Давайте создадим своего первого зверька")
print("Для этого напишите команду create и его имя -> нажмите Enter")
while running:
    for key in bestiary:
        bestiary[key].state_check()
    a = input(" $: ")
    if len(a.split()) == 2 and a.split()[0] == "create":
        bestiary.update({a.split()[1]: tamagochi(a.split()[1])})
        print("Шикарно! Вы всегда можете проверить ваш бестиарий с помошью команды LS")
        print("для того чтобы поиграть со зверьком команду play и имя зверя")
        print("Аналогично работает и с feed, + в конце указывается число еды")
    elif len(a.split()) == 1 and a.split()[0] == "create":
        print("Нужно имя!")
    if a == "LS":
        # LSprint(bestiary)
        k = 0
        for key in bestiary:
            k += 1
            print(k, bestiary[key])
    if len(a.split()) == 3 and a.split()[0] == "feed":
        if bestiary.get(a.split()[1], False):
            bestiary.get(a.split()[1]).eat(int(a.split()[2]))
    if len(a.split()) == 2 and a.split()[0] == "play":
        if bestiary.get(a.split()[1], False):
            bestiary.get(a.split()[1]).play()
