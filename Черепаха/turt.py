import turtle
import math
turtle.speed(0)

def polygon(sides,length):
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)
    #turtle.forward(3)
    #turtle.left(5)
    if length<1:
        return False
    polygon(sides,length-3)


def clever(n,dem):
    angle= (n-2)/n * 180
    radius=dem/(2* math.tan(math.pi/n))
    forw=math.floor(radius-0.3*radius)
    #print(angle)
    angle=180-angle
    #print(angle)
    polygon(n,dem)
    turtle.left(180)
    polygon(n,dem)
    turtle.right(angle/2)
    turtle.forward(forw)
    turtle.right(90-angle/2)
    polygon(n,dem)
    turtle.width(2)
    turtle.right(90+angle/2)
    turtle.forward(3*radius)
    turtle.width(1)
    
n=6
dem=15
turtle.Screen().bgcolor(0.25,0.30,0.20)
turtle.pen(fillcolor="green", pencolor="lightgreen",)



for i in range (0,500,100):
    for j in range(-300,500,100):
        turtle.up()
        turtle.setpos(i,j)
        turtle.down()
        clever(6,15)
        
