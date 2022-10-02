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
        self.__satiety = State.Normal
        self.__satisfaction = Satisfaction.Nice

    def __str__(self):
        return str(f"Name: {self.__name}, Status:  {self.__satiety} (-1 to 5), Satisfaction:  {self.__satisfaction} (0 to 2)")

    def add_satiety(self, count):
        if self.__satiety != State.Dead:
            self.__satiety += count
            self.__st = dt.now()
        if self.__satiety > State.Cheerful:
            self.__satiety = State.Cheerful

    def set_satiety(self, satiety):
        self.__satiety = satiety

    def get_satiety(self):
        return self.__satiety
    satiety = property(get_satiety, set_satiety)

    def get_name(self):
        return self.__name
    name = property(get_name)

    def play(self):
        if self.__satiety != State.Dead:
            self.__satisfaction += 1
        if self.__satiety > Satisfaction.Euphoria:
            self.__satisfaction = Satisfaction.Euphoria

    def state_check(self):
        # смерть?
        if self.__satiety == State.Dead:
            self.anigilation()
        # если нет то голодание
        elif (delta := ((dt.now()-self.__st).seconds)) >= self.__eat_timeout and self.__satiety != State.Dead:
            self.__satiety -= delta//self.__eat_timeout
            self.__st = dt.now()
            if self.__satiety < State.Dead:
                self.__satiety = State.Dead

    def anigilation(self):
        # функция смерти
        if self.__flag == True:
            self.__satisfaction = "in heaven with happiness"
            print(f"Зверь {self.__name} умер!\n $: ")
            self.__flag = False


def state_str():
    # вывод характеристик
    k = 0
    for key in bestiary:
        k += 1
        print(k, bestiary[key])
    if k == 0:
        print("⚠ Бестиарий пуст!")


running = True
bestiary = {}
print("Приветствую!, Давайте создадим своего первого зверька")
print("Для этого напишите команду create и его имя -> нажмите Enter")
while running:
    for key in bestiary:
        bestiary[key].state_check()
    a = input(" $: ")
    # проверка ввода пользователя
    # #создание экзэмпляра зверька
    if len(a.split()) == 2 and a.split()[0] == "create":
        bestiary.update({a.split()[1]: tamagochi(a.split()[1])})
        print("Шикарно! Вы всегда можете проверить ваш бестиарий с помошью команды ls")
        print("для того чтобы поиграть со зверьком команду play и имя зверя")
        print("Аналогично работает и с feed, + в конце указывается число еды")
    elif len(a.split()) == 1 and a.split()[0] == "create":
        print("Нужно имя!")
    # список зверьков с информацией
    if a == "ls":
        # LSprint(bestiary)
        state_str()
    # #кормежка и поилка
    if len(a.split()) == 3 and a.split()[0] == "feed":
        if bestiary.get(a.split()[1], False):
            bestiary.get(a.split()[1]).add_satiety(int(a.split()[2]))
        else:
            print("⚠ Такого зверя нет!")
        state_str()
    if len(a.split()) == 2 and a.split()[0] == "play":
        if bestiary.get(a.split()[1], False):
            bestiary.get(a.split()[1]).play()
        else:
            print("⚠ Такого зверя нет!")
        state_str()
