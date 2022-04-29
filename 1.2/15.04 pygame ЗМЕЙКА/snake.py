from tkinter import messagebox
import tkinter as tk
import random
import math
import pygame


class snake():

    def __init__(self, pos_start):
        self.head = pos_start
        self.body = [[100, 50],
                     [90, 50],
                     [80, 50],
                     [70, 50]
                     ]
        self.speed = 15
        self.direction = "RIGHT"
        self.change_dir = self.direction

    def move(self, game_window):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_dir = 'UP'
                if event.key == pygame.K_DOWN:
                    self.change_dir = 'DOWN'
                if event.key == pygame.K_LEFT:
                    self.change_dir = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    self.change_dir = 'RIGHT'
        if self.change_dir == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_dir == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_dir == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_dir == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        if self.direction == 'UP':
            self.head[1] -= 10
        if self.direction == 'DOWN':
            self.head[1] += 10
        if self.direction == 'LEFT':
            self.head[0] -= 10
        if self.direction == 'RIGHT':
            self.head[0] += 10
        self.body.insert(0, list(self.head))
        self.body.pop()
        for pos in self.body:
            pygame.draw.rect(game_window, (0, 255, 0),
                             pygame.Rect(pos[0], pos[1], 10, 10))


pygame.init()


def main():

    window_x = 720
    window_y = 480
    game_window = pygame.display.set_mode((window_x, window_y))
    game_over = False

    fps = pygame.time.Clock()
    s = snake([100, 50])
    score = 0
    while not game_over:
        s.move(game_window)
        pygame.display.update()
        fps.tick(s.speed)


main()
