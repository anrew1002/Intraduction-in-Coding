from threading import Thread
import time


class Test():
    def counting(self):
        global running
        print("\n5\n:&!")


def inputing():
    x = input(":&")


a = Test()
running = True
while running:
    th = Thread(target=inputing)
    th.start()
    a.counting()
