import turtle
import random
from datetime import datetime
import math

#zmienne: długość, kolor linii, kolor wypełnienia, współrzędna x, współrzędna y, kąt

def square(s,color1,color01,x1,y1,angel1):
    turtle.pencolor(color1)
    turtle.fillcolor(color01)
    if z==0:
        turtle.penup()
        turtle.setpos(x1,y1)
        turtle.pendown()
    else:
        turtle.penup()
        turtle.setpos(x1,y1-(s*z)-(20*z))
        turtle.pendown()
    turtle.begin_fill()
    turtle.right(angel1)
    for x in range(4):
        turtle.forward(s)
        turtle.left(90)
    turtle.end_fill()
    turtle.left(angel1)

def right(a,color2,color02,x2,y2,angel2):
    b=a*math.sqrt(2)
    turtle.pencolor(color2)
    turtle.fillcolor(color02)
    if z==0:
        turtle.penup()
        turtle.setpos(x2,y2+a)
        turtle.pendown()
    else:
        turtle.penup()
        turtle.setpos(x2,y2+a-(a*z)-(20*z))
        turtle.pendown()
    turtle.right(90+angel2)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(a)
        turtle.left(90)
    turtle.left(45)
    turtle.forward(b)
    turtle.end_fill()
    turtle.right(135-angel2)
    
    


def cross(c,color3,color03,x3,y3,angel3):
    turtle.pencolor(color3)
    turtle.fillcolor(color03)
    if z==0:
        turtle.penup()
        turtle.setpos(x3,y3+0.85*c)
        turtle.pendown()
    else:
        turtle.penup()
        turtle.setpos(x3,y3+0.85*c-(3*c*z)-(20*z))
        turtle.pendown()
    turtle.begin_fill()
    turtle.right(angel3)
    for x in range(4):
        turtle.right(90)
        turtle.forward(c)
        turtle.left(90)
        turtle.forward(c)
        turtle.left(90)
        turtle.forward(c)
    turtle.end_fill()
    turtle.left(angel3)
    
def rhombus(d,color4,color04,x4,y4,angel4):
    turtle.pencolor(color4)
    turtle.fillcolor(color04)
    if z==0:
        turtle.penup()
        turtle.setpos(x4,y4+0.7*d)
        turtle.pendown()
    else:
        turtle.penup()
        turtle.setpos(x4+3*z,y4+0.7*d-(2*d*z)-(10*z))
        turtle.pendown()
    turtle.right(50+angel4)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(d)
        turtle.left(100)
        turtle.forward(d)
        turtle.left(80)
    turtle.end_fill()
    turtle.left(50+angel4)
    

def trefoil(f,color5,color05,x5,y5,angel5):
    turtle.pencolor(color5)
    turtle.fillcolor(color05)
    if z==0:
        turtle.penup()
        turtle.setpos(x5,y5+3*f)
        turtle.pendown()
    else:
        turtle.penup()
        turtle.setpos(x5,y5+3*f-(17*f*z)-(20*z))
        turtle.pendown()
    turtle.begin_fill()
    turtle.right(angel5)
    for y in range(3):
        for x in range(17):
            turtle.forward(f)
            turtle.left(12)
        turtle.right(84)
    turtle.end_fill()
    turtle.left(angel5)
    
def name():
    turtle.penup()
    turtle.setpos(340,350)
    turtle.write("Wiktoria Sadło, ZZISS1-1113")


def kolor():
    y="#"
    for x in range(6):
        y+=random.choice("ABCDEF0123456789")
    return y


def time():
    turtle.penup()
    turtle.setpos(350,-200)
    turtle.pendown()
    turtle.write(now2-now1)

#color=["#"+"".join(random.choice("ABCDEF0123456789") for x in range (6))]

#zmienne: długość, kolor linii, kolor wypełnienia, współrzędna x, współerzędna y, kąt nachylenia
now1 = datetime.now()
name()
for z in range(4):
    square(70,kolor(),kolor(),-400,200,0)
    right(70,kolor(),kolor(),-250,200,0)
    cross(23,kolor(),kolor(),-100,200,0)
    rhombus(40,kolor(),kolor(),25,200,0)
    trefoil(4,kolor(),kolor(),200,200,25)
now2 = datetime.now()
time()
turtle.done()
