import pygame as pg
# import tkinter as tk
# from tkinter.ttk import *
from pygame.locals import (QUIT)
import random


class Planet():
    def __init__(self, radius, color, speed, colocation):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.colocation = (500, 500-colocation)

    def draw_yourself(self, sc):
        pg.draw.circle(sc, self.color, self.colocation, self.radius)


# радиус, цвет, скорость, дальность от солнца
earth_r = 4
a_e = 4
sun = Planet(5, (255, 20, 20), 10, 0)
mercury = Planet(
    round(earth_r*0.38240827845719661335841956726246), (200, 20, 20), 10, round(58/a_e))
venus = Planet(round(earth_r*0.94873000940733772342427093132643),
               (200, 20, 20), 10, round(108.9/a_e))
earth = Planet(earth_r, (20, 20, 255), 10, round(149.6/a_e))
mars = Planet(earth_r*0.53135779241141423643775478206334,
              (20, 20, 80), 10, round(228/a_e))
jupiter = Planet(earth_r*11.209156475384132957039824396362,
                 (20, 80, 255), 10, round(741*0.7/a_e))
saturn = Planet(earth_r*9.4543744120413922859830667920978,
                (80, 20, 205), 10, round(1430*0.7/a_e))
uranus = Planet(earth_r*3.9761680777673251803073063656319,
                (20, 90, 90), 10, round((2800-1500)/a_e))
neptune = Planet(earth_r*3.8604578237692066478519912198181,
                 (20, 100, 255), 10, round((4500-2700)/a_e))


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Solar System")
clock = pg.time.Clock()

print(sun.color, mercury.radius)

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == QUIT:
            # print(event.type)
            running = False
    screen.fill((185, 177, 219))
    sun.draw_yourself(screen)
    mercury.draw_yourself(screen)
    venus.draw_yourself(screen)
    earth.draw_yourself(screen)
    mars.draw_yourself(screen)
    jupiter.draw_yourself(screen)
    saturn.draw_yourself(screen)
    uranus.draw_yourself(screen)
    neptune.draw_yourself(screen)
    pg.display.update()


pg.quit()
