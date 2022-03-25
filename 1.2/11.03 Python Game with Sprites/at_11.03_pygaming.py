import pygame as pg
import tkinter as tk
from tkinter.ttk import *
from pygame.locals import ( K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT,)
import random

def playerInit():
    global playerSprite
    playerSprite.image=pygame.Surface((45,45))
    playerSprite.image.fill((255,255,255))
    playerSprite.rect=playerSprite.image.get_rect()

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
FPS=60
enemySpeed=5
class MyPlayer(pg.sprite.Sprite):
    def __init__(self,x,filename):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(filename).convert_alpha()
        self.rect=self.image.get_rect(center=(x,200))
    def update(self,keys):
        if keys[K_UP]:
            self.rect.move_ip(0,-5)
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            
class Enemy(pg.sprite.Sprite):
    def __init__(self,y,filename):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(filename).convert_alpha()
        self.rect=self.image.get_rect(center=(700,y))
    def update(self):    
        self.rect.move_ip(-enemySpeed,0)
        if self.rect.right<0:
            self.rect=self.image.get_rect(center=(random.randint(SCREEN_WIDTH+20,SCREEN_WIDTH+100),
                                                 random.randint(0,SCREEN_HEIGHT)))
            
        
            




    
pg.init()
screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("My Game")
clock=pg.time.Clock()

screen.fill((185,177,219))

player1=MyPlayer(300,"player.png")
enemies=pg.sprite.Group()
enemy1=Enemy(random.randint(0,SCREEN_HEIGHT),"enemy1.png")
enemy2=Enemy(random.randint(0,SCREEN_HEIGHT),"enemy2.png")
enemy3=Enemy(random.randint(0,SCREEN_HEIGHT),"enemy1.png")
enemies.add(enemy1)
enemies.add(enemy2)
enemies.add(enemy3)

running = True
while running:
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type==QUIT:
            #print(event.type)
            running=False
        
    screen.fill((185,177,219))
    screen.blit(player1.image,player1.rect)
    screen.blit(enemy1.image,enemy1.rect)
    screen.blit(enemy2.image,enemy2.rect)
    screen.blit(enemy3.image,enemy3.rect)
            
    pg.display.flip()

    keys=pg.key.get_pressed()
    player1.update(keys)
    enemy1.update()
    enemy2.update()
    enemy3.update()
    if pg.sprite.spritecollide(player1,enemies,True):
        running=False
root = tk.Tk()
label = tk.Label(root, text="Вы проиграли", height=5,width=40)
label.pack()
    

    
pg.quit()

