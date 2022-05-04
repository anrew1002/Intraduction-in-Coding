from email.mime import image
from tkinter import *
import random
from turtle import color
from numpy import outer
import pygame
import copy

pygame.mixer.pre_init(frequency=44100, size=8, channels=2,
                      buffer=512, devicename=None)
pygame.init()
pygame.mixer.music.load("YoshidaBrothersNabbed.mp3")
s_hrum = pygame.mixer.Sound('hrum1.wav')
sound_bum = pygame.mixer.Sound('bum.wav')

# ИГРА:


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

        for pos in self.body:
            pygame.draw.rect(game_window, (0, 255, 0),
                             pygame.Rect(pos[0], pos[1], self.size, self.size))
        for block in self.body[1:]:
            if self.head[0] == block[0] and self.head[1] == block[1]:
                game_over_window(score, game_window)

    def crawl(self):
        self.body.pop()


class EnemySnake():
    def __init__(self, pos_start, cell_size, speed):
        self.size = cell_size
        self.head = pos_start
        pos_start = copy.deepcopy(pos_start)
        self.body = [pos_start,
                     [pos_start[0]+(self.size*1), pos_start[1]],
                     [pos_start[0]+(self.size*2), pos_start[1]],
                     [pos_start[0]+(self.size*3), pos_start[1]]
                     ]
        self.speed = speed
        self.direction = "LEFT"
        self.change_dir = self.direction

    def move(self, fruit_pos, game_window):
        self.change_dir = random_direction(self.head, fruit_pos)
        print("1", self.change_dir)
        self.head = pos_add(direction_check(
            self.change_dir, self.direction), self.head, self.size)

        self.body.insert(0, list(self.head))

        for pos in self.body:
            pygame.draw.rect(game_window, (255, 255, 0),
                             pygame.Rect(pos[0], pos[1], self.size, self.size))

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

    def redraw(self, placed):
        self.pos = random_pos(self.size)
        while self.pos in placed:
            self.pos = random_pos(self.size)
        self.draw()


class barricade():
    def __init__(self, game_window, cell_size, position):
        self.locations_of = []
        self.window = game_window
        self.size = cell_size
        self.pos = position

    def draw(self):
        for pos in self.pos:
            pygame.draw.rect(self.window, (255, 50, 0), pygame.Rect(
                pos[0], pos[1], self.size, self.size))
            self.locations_of.append(pos)


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
# --------------

# ОСНОВНОЙ ЦИКЛ:


def main(event, root):

    global score, window_x, window_y, cell_size
    root.destroy()
    game_window = pygame.display.set_mode((window_x, window_y))
    is_game_over = False
    pygame.mixer.music.play(loops=0, start=0.0,
                            fade_ms=0)
    fps = pygame.time.Clock()
    s = Snake([100, 50], cell_size, 15)
    f = Fruit(game_window, cell_size)
    enemy1 = EnemySnake([200, 300], cell_size, 14)
    block = barricade(game_window, cell_size, [[50, 55], [50, 60], [50, 65]])

    while not is_game_over:
        game_window.fill((0, 0, 0))
        enemy1.move(f.pos, game_window)
        s.move(game_window)

        block.draw()
        f.draw()
        if s.head[0] == f.pos[0] and s.head[1] == f.pos[1]:
            s_hrum.play()
            score += 10
            f.redraw(s.body+enemy1.body+block.locations_of)
        else:
            s.crawl()
        if enemy1.head[0] == f.pos[0] and enemy1.head[1] == f.pos[1]:
            f.redraw(s.body+enemy1.body+block.locations_of)
        else:
            enemy1.crawl()
        if s.head[0] < 0 or s.head[0] > window_x-cell_size:
            sound_bum.play()
            game_over_window(score, game_window)
        if s.head[1] < 0 or s.head[1] > window_y-cell_size:
            sound_bum.play()
            game_over_window(score, game_window)

        pygame.display.update()
        fps.tick(s.speed)

# Программные функции!:


def random_direction(head, fruit):
    i = random.randint(1, 4)
    direction = ""

    if (i == 1) or (abs(head[0]-fruit[0]) < 6) or (abs(head[1]-fruit[1]) < 6):
        if head[0] < fruit[0]:
            direction = "RIGHT"
        if head[0] > fruit[0]:
            direction = "LEFT"
        if head[1] < fruit[1]:
            direction = "DOWN"
        if head[1] > fruit[1]:
            direction = "UP"

    else:
        if head[1] < fruit[1]:
            direction = "DOWN"
        if head[1] > fruit[1]:
            direction = "UP"
        if head[0] < fruit[0]:
            direction = "RIGHT"
        if head[0] > fruit[0]:
            direction = "LEFT"
    return direction


def direction_check(change, dir):
    if change == 'UP' and dir != 'DOWN':
        dir = 'UP'
    if change == 'DOWN' and dir != 'UP':
        dir = 'DOWN'
    if change == 'LEFT' and dir != 'RIGHT':
        print("LEFT")
        dir = 'LEFT'
    if change == 'RIGHT' and dir != 'LEFT':
        print("RIGHT")
        dir = 'RIGHT'

    output = [0, 0, 0, 0]
    if dir == "UP":
        output[0] = 1
    if dir == "DOWN":
        output[1] = 1
    if dir == "LEFT":
        output[2] = 1
    if dir == "RIGHT":
        output[3] = 1
    return output


def pos_add(coef, head, size):
    head = copy.deepcopy(head)
    head[1] -= size*coef[0]
    head[1] += size*coef[1]
    head[0] -= size*coef[2]
    head[0] += size*coef[3]
    return head


def random_pos(size):
    return [random.randrange(1, (window_x//size)) * size,
            random.randrange(1, (window_y//size)) * size]


def on_closing():
    pygame.quit()
    quit()
# --------------

# ФУНКЦИИ МЕНЮ:


def menu_main():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
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
# -------------------------


window_x = 720
window_y = 480
score = 0
cell_size = 5

menu_main()
