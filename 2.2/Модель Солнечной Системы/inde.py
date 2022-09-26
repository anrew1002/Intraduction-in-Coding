from re import S
import pygame as pg
# import tkinter as tk
# from tkinter.ttk import *
from pygame.locals import (QUIT)
import random
import math


class Planet():
    def __init__(self, radius, color, speed, colocation):
        global origin
        self.radius = radius
        self.color = color
        self.speed = speed
        self.origin = origin
        self.colocation = colocation
        self.cordinates = (origin[0], origin[1]-colocation)
        self.angle = 0

    def draw_yourself(self, sc):
        pg.draw.circle(sc, self.color, self.cordinates, self.radius)

    def align(self, sc, t):
        self.angle = t*self.speed
        x = self.colocation*math.cos(self.angle)
        y = self.colocation*math.sin(self.angle)
        self.cordinates = (self.origin[0]+x, self.origin[1]+y)
        self.draw_yourself(sc)


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
origin = (500, 500)
FPS = 60

# радиус, цвет, скорость, дальность от солнца
earth_r = 4
ea_speed = 0.5
a_e = 4

sun = Planet(5, (255, 20, 20), 10, 0)
mercury = Planet(
    round(earth_r*0.38240827845719661335841956726246), (200, 20, 20), 1/0.241095*ea_speed, round(58/a_e))
venus = Planet(round(earth_r*0.94873000940733772342427093132643),
               (200, 20, 20), 1/0.6136986*ea_speed, round(108.9/a_e))
earth = Planet(earth_r, (20, 20, 255), ea_speed, round(149.6/a_e))
mars = Planet(earth_r*0.53135779241141423643775478206334,
              (20, 20, 80), 0.53137283*ea_speed, round(228/a_e))
jupiter = Planet(earth_r*11.209156475384132957039824396362,
                 (20, 80, 255), 1/11.89*ea_speed, round(741*0.7/a_e))
saturn = Planet(earth_r*9.4543744120413922859830667920978,
                (80, 20, 205), 1/29.46*ea_speed, round(1430*0.7/a_e))
uranus = Planet(earth_r*3.9761680777673251803073063656319,
                (20, 90, 90), 1/84*ea_speed, round((2800-1500)/a_e))
neptune = Planet(earth_r*3.8604578237692066478519912198181,
                 (20, 100, 255), 1/164.79*ea_speed, round((4500-2700)/a_e))


pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Solar System")
clock = pg.time.Clock()

print(sun.color, mercury.radius)

running = True
t = 0
while running:
    t += 0.2
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == QUIT:
            # print(event.type)
            running = False
    screen.fill((185, 177, 219))
    sun.draw_yourself(screen)
    mercury.align(screen, t)
    venus.align(screen, t)
    earth.align(screen, t)
    mars.align(screen, t)
    jupiter.align(screen, t)
    saturn.align(screen, t)
    uranus.align(screen, t)
    neptune.align(screen, t)
    pg.display.update()


pg.quit()
