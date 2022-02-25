import pygame as pg
from pygame.locals import ( K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT,)

def playerInit():
    global playerSprite
    playerSprite.image=pygame.Surface((45,45))
    playerSprite.image.fill((255,255,255))
    playerSprite.rect=playerSprite.image.get_rect()

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
FPS=60

class myplayer(pg.sprite.Sprite):
    SCREEN_WIDTH=600
    SCREEN_HEIGHT=600
    def __init__(self,x,filename):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(filename).convert_alpha()
        self.rect=self.image.get_rect(center=(x,200))
    def update(self,keys):
        if self.rect.y < SCREEN_HEIGHT:
            if keys[K_UP]:
                self.rect.move_ip(0,-5)
            if keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.x < SCREEN_WIDTH:
            if keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    

pg.init()
screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("My Game")
clock=pg.time.Clock()

screen.fill((185,177,219))

player1=myplayer(300,"player.png")

running = True
while running:
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type==QUIT:
            #print(event.type)
            running=False
        
    screen.fill((185,177,219))
    screen.blit(player1.image,player1.rect)      
            
    pg.display.flip()

    keys=pg.key.get_pressed()
    player1.update(keys)
    




    
pg.quit()
