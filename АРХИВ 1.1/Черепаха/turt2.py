import math
import turtle
turtle.speed(0)
turtle.Screen().bgcolor("#FF3355")
turtle.color("#FDFDFD")
turtle.hideturtle()

a=100
k=1.25
turtle.up()
i=0
while i <2000:
    koef=math.sin(math.radians(k*i))
    if abs(koef) < 0.9:
        i+=2
    p= a * (koef)
    turtle.forward(p)
    
    turtle.dot(5,"white")
    
    turtle.setpos(0,0)
    if abs(koef) < 0.9:
        turtle.left(3)
    else:
        turtle.left(1)
    i+=1
    print(i)
    
turtle.setpos(0,-200)

turtle.write("ARASAKA", align="center", font=("Consolas",34,"normal"))

    
    
    
    
