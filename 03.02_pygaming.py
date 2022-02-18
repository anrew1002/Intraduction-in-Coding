import pygame
from pygame.locals import ( K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT,)
def coloring(col,iteration):
    import random
    seting= random.randint(1,2)
    colLi=list(col)
    if iteration:
        colLi[1]=colLi[1]-colLi[1]*random.randint(5,9)/50
    elif not iteration:
        
        colLi=[240,58,64]
        colLi[0]=colLi[0]-colLi[0]*random.randint(5,9)/50
        if seting==2:
            colLi=[222,252,48]
            colLi[1]=colLi[1]-colLi[1]*random.randint(1,7)/50
            
    print(colLi)
    return list(map(int,colLi))
def paint_tree(iteration):
    
    color=[0,250,0]
    
    pygame.draw.circle(screen, coloring(color,iteration), (371, 235), 45)
    pygame.draw.circle(screen,  coloring(color,iteration), (347, 164), 25)
    pygame.draw.circle(screen,  coloring(color,iteration), (304, 251), 39)
    pygame.draw.circle(screen,  coloring(color,iteration), (309, 303), 39)
    pygame.draw.circle(screen,  coloring(color,iteration), (368, 311), 14)
    pygame.draw.circle(screen,  coloring(color,iteration), (312, 99), 24)
    pygame.draw.circle(screen,  coloring(color,iteration), (255, 142), 35)
    pygame.draw.circle(screen,  coloring(color,iteration), (192, 160), 70)
    pygame.draw.circle(screen,  coloring(color,iteration), (221, 231), 39)
    pygame.draw.circle(screen,  coloring(color,iteration), (178, 267), 34)
    pygame.draw.line(screen, (107,45,15),(263,459),(263,270),4)
    pygame.draw.line(screen, (107,45,15),(263,270),(282,253),5)
    pygame.draw.line(screen, (107,45,15),(263,270),(266,181),4)
    pygame.draw.line(screen, (107,45,15),(267,237),(244,218),5)
    pygame.display.flip()
    
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

screen.fill((0, 150, 189))

iteration=True
paint_tree(iteration)

TreeRect=pygame.Rect(119,64,300,406)



running = True
while running:
    print(pygame.mouse.get_pos())
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if TreeRect.collidepoint(x,y):  
                paint_tree(iteration)
    #if not iteration:
        #screen.fill((179, 25, 97))
    #if iteration:
        #screen.fill((0, 150, 189))
    iteration= not iteration
        
   
pygame.quit()
