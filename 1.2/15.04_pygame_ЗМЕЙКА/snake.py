from tkinter import *
import random
import math
import pygame
import time

pygame.init()


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
        global window_x, window_y, score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
        game_window.fill((0, 0, 0))
        for pos in self.body:
            pygame.draw.rect(game_window, (0, 255, 0),
                             pygame.Rect(pos[0], pos[1], 10, 10))
        for block in self.body[1:]:
            if self.head[0] == block[0] and self.head[1] == block[1]:
                game_over_window(score, game_window)

    def crawl(self):
        self.body.pop()


class fruit():
    def __init__(self,  game_window, is_spawn=True):
        self.window = game_window
        self.spawn = is_spawn
        self.pos = random_pos()
        self.draw()

    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(
            self.pos[0], self.pos[1], 10, 10))

    def redraw(self):
        self.pos = random_pos()
        self.draw()


def game_over_window(score, game_window):
    global window_x, window_y

    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    menu_main()


def main(event, root):

    global score, window_x, window_y
    root.destroy()
    game_window = pygame.display.set_mode((window_x, window_y))
    is_game_over = False

    fps = pygame.time.Clock()
    s = snake([100, 50])
    f = fruit(game_window)

    while not is_game_over:
        s.move(game_window)
        f.draw()
        if s.head[0] == f.pos[0] and s.head[1] == f.pos[1]:
            score += 10
            f.redraw()
        else:
            s.crawl()

        if s.head[0] < 0 or s.head[0] > window_x-10:
            game_over_window(score, game_window)
        if s.head[1] < 0 or s.head[1] > window_y-10:
            game_over_window(score, game_window)
        pygame.display.update()
        fps.tick(s.speed)


def random_pos():
    return [random.randrange(1, (window_x//10)) * 10,
            random.randrange(1, (window_y//10)) * 10]


def menu_main():
    root = Tk()
    bg = PhotoImage(file="15.04_pygame_ЗМЕЙКА/bck.png")
    but_play = Button(text='Play')
    but_play.bind("<Button-1>", lambda e, fun=root: main(e, fun))
    but_play.pack()
    root.mainloop()


window_x = 720
window_y = 480
score = 0

menu_main()


main()
