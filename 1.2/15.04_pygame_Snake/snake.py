from email.mime import image
from tkinter import *
import random
import math
from turtle import color
import pygame
import time
import copy

pygame.mixer.pre_init(frequency=44100, size=8, channels=2,
                      buffer=512, devicename=None)
pygame.init()
pygame.mixer.music.load("YoshidaBrothersNabbed.mp3")
s_hrum = pygame.mixer.Sound('hrum1.wav')
sound_bum = pygame.mixer.Sound('bum.wav')


class Snake():

    def __init__(self, pos_start, cell_size, speed):
        self.size = cell_size
        self.head = pos_start
        pos_start = copy.deepcopy(pos_start)
        self.body = [pos_start,
                     [pos_start[0]-(self.size*1), pos_start[1]],
                     [pos_start[0]-(self.size*2), pos_start[1]],
                     [pos_start[0]-(self.size*3), pos_start[1]]
                     ]
        self.speed = speed
        self.direction = "RIGHT"
        self.change_dir = self.direction

    def move(self, game_window):
        global window_x, window_y, score

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
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
            self.head[1] -= self.size
        if self.direction == 'DOWN':
            self.head[1] += self.size
        if self.direction == 'LEFT':
            self.head[0] -= self.size
        if self.direction == 'RIGHT':
            self.head[0] += self.size
        self.body.insert(0, list(self.head))
        game_window.fill((0, 0, 0))
        for pos in self.body:
            pygame.draw.rect(game_window, (0, 255, 0),
                             pygame.Rect(pos[0], pos[1], self.size, self.size))
        for block in self.body[1:]:
            if self.head[0] == block[0] and self.head[1] == block[1]:
                game_over_window(score, game_window)

    def crawl(self):
        self.body.pop()


class Fruit():
    def __init__(self,  game_window, cell_size, is_spawn=True, ):
        self.window = game_window
        self.spawn = is_spawn
        self.pos = random_pos(cell_size)
        self.size = cell_size
        self.draw()

    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(
            self.pos[0], self.pos[1], self.size, self.size))

    def redraw(self):
        self.pos = random_pos(self.size)
        self.draw()


def game_over_window(score, game_window):
    global window_x, window_y
    pygame.mixer.music.stop()
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    menu_main()


def main(event, root):

    global score, window_x, window_y, sell_size
    root.destroy()
    game_window = pygame.display.set_mode((window_x, window_y))
    is_game_over = False
    pygame.mixer.music.play(loops=0, start=0.0,
                            fade_ms=0)
    fps = pygame.time.Clock()
    s = Snake([100, 50], sell_size, 15)
    f = Fruit(game_window, sell_size)

    while not is_game_over:
        s.move(game_window)
        f.draw()
        if s.head[0] == f.pos[0] and s.head[1] == f.pos[1]:
            s_hrum.play()
            score += 10
            f.redraw()
        else:
            s.crawl()

        if s.head[0] < 0 or s.head[0] > window_x-sell_size:
            sound_bum.play()
            game_over_window(score, game_window)
        if s.head[1] < 0 or s.head[1] > window_y-sell_size:
            sound_bum.play()
            game_over_window(score, game_window)

        pygame.display.update()
        fps.tick(s.speed)


def random_pos(size):
    return [random.randrange(1, (window_x//size)) * size,
            random.randrange(1, (window_y//size)) * size]


def menu_main():
    root = Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = (w//2)-200
    h = (h//2)-200
    root.geometry("400x400+{}+{}".format(w, h))
    root.resizable(False, False)
    bg = PhotoImage(file="bck.png")
    canvas1 = Canvas(root, width=400, height=400)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")

    but_play = Button(text='Play', width=15, height=3)
    but_proper = Button(text="Properties", width=15, height=3)
    but_rules = Button(text="Rules", width=15, height=3)
    but_play.bind("<Button-1>", lambda e, fun=root: main(e, fun))
    but_proper.bind("<Button-1>", lambda e, fw=w,
                    fh=h, bgg=bg: menu_proper(e, fw, fh, bgg))
    but_rules.bind("<Button-1>", lambda e, fh=h, fw=w,
                   bgg=bg: menu_rules(e, fw, fh, bgg))
    button_play_canv = canvas1.create_window(
        140, 30, anchor="nw", window=but_play)
    but_proper_canv = canvas1.create_window(
        140, 100, anchor="nw", window=but_proper)
    but_rules_canv = canvas1.create_window(
        140, 170, anchor="nw", window=but_rules)

    root.mainloop()


def menu_proper(event, w, h, bg):
    def change_window_size(event, new_x, new_y):
        global window_x, window_y
        window_x = new_x
        window_y = new_y

    proper = Toplevel()
    proper.geometry("400x400+{}+{}".format(w, h))
    canvas2 = Canvas(proper, width=400, height=400)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg, anchor="nw")

    but_1080x1080 = Button(proper, text="1080x1080", height=2, width=9)
    but_1080x1080.bind("<Button-1>", lambda e, x=1080,
                       y=1080: change_window_size(e, x, y))
    button_1080x1080_canv = canvas2.create_window(
        140, 100, anchor="nw", window=but_1080x1080)

    but_800x800 = Button(proper, text="800x800", height=2, width=9)
    but_800x800.bind("<Button-1>", lambda e, x=800,
                     y=800: change_window_size(e, x, y))
    button_800x800_canv = canvas2.create_window(
        140, 150, anchor="nw", window=but_800x800)

    but_720x480 = Button(proper, text="720x480", height=2, width=9)
    but_720x480.bind("<Button-1>", lambda e, x=720,
                     y=480: change_window_size(e, x, y))
    button_720x480_canv = canvas2.create_window(
        140, 200, anchor="nw", window=but_720x480)

    but_escp = Button(proper, text="Back", height=1, width=5)
    but_escp.bind("<Button-1>", lambda e, pr=proper: pr.destroy())
    but_ecp_canv = canvas2.create_window(10, 10, anchor="nw", window=but_escp)
    proper.mainloop()


def menu_rules(event, w, h, bg):
    ruler = Toplevel()
    ruler.geometry("400x400+{}+{}".format(w, h))
    canvas3 = Canvas(ruler, width=400, height=400)
    canvas3.pack(fill="both", expand=True)
    canvas3.create_image(0, 0, image=bg, anchor="nw")

    canvas3.create_text(
        70, 60, anchor="nw", text="Используйте клавиши WASD,\nдля того чтобы съесть яблочки,\nи подрасти.\nНи во что не врезайтесь!", font=("Helvetica", 14, "bold"), fill="white")
    but_escp = Button(ruler, text="Back", height=1, width=5)
    but_escp.bind("<Button-1>", lambda e, pr=ruler: pr.destroy())
    but_ecp_canv = canvas3.create_window(10, 10, anchor="nw", window=but_escp)


window_x = 720
window_y = 480
score = 0
sell_size = 5

menu_main()
