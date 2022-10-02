import pygame as pg
from pygame.locals import (QUIT)
import math


class Planet():
    def __init__(self, name, radius, color, speed, colocation):
        global origin
        self.__name = name
        self.__radius = radius // 1594.5
        self.__color = color
        self.__speed = 1/speed * scale_radius
        self.__origin = origin
        self.__colocation = colocation * scale_a_e
        self.__cordinates = (origin[0], origin[1]-colocation)
        self.__angle = 0

    @property
    def name(self):
        return self.__name

    @property
    def radius(self):
        return self.__radius * 1594.5

    @property
    def angle(self):
        '''Угол в градусах'''
        return self.__angle * 57.2958

    def set_colacation(self, value):
        self.__colocation = value

    def get_colacation(self):
        return self.__colocation
    colocation = property(get_colacation, set_colacation)

    def draw_yourself(self, sc):
        pg.draw.circle(sc, self.__color, self.__cordinates, self.__radius)

    def align(self, sc, t):
        self.__angle = t*self.__speed
        x = self.__colocation*math.cos(self.__angle)
        y = self.__colocation*math.sin(self.__angle)
        self.__cordinates = (self.__origin[0]+x, self.__origin[1]+y)
        self.draw_yourself(sc)


scale_a_e = float(input("введите масштаб расстояний (рекомендую число 0.2): "))
scale_radius = float(input("введите масштаб планет (рекомендую число 0.2): "))

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
origin = [500, 500]
FPS = 60

dict_planet = []

with open("input.txt", "r", encoding="UTF-8") as f:
    f.readline()
    f = f.readlines()
    for line in f:
        line = line.strip().split()
        dict_planet.append(
            Planet(line[0], float(line[1]), tuple(map(int, line[4][1:-1].split(","))), float(line[2]), float(line[3]), ))

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Solar System")
clock = pg.time.Clock()
# dict_planet[8].colocation = dict_planet[8].colocation
# print(dict_planet[0].colocation)

running = True
t = 0
while running:
    t += 0.2
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if origin[1] < 1000:
                    origin[1] += 100
            if event.key == pg.K_DOWN:
                if origin[1] > 0:
                    origin[1] -= 100
            if event.key == pg.K_LEFT:
                if origin[0] < 1000:
                    origin[0] += 100
            if event.key == pg.K_RIGHT:
                if origin[0] > 0:
                    origin[0] -= 100
            # print(dict_planet[6].name, dict_planet[6].angle)
    screen.fill((185, 177, 219))
    for planet in dict_planet:
        planet.align(screen, t)
    pg.display.update()

pg.quit()
