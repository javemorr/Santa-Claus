Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Thanks Dr. Ray to teach us to code with Python!

import turtle as t

t.penup()
t.shape('turtle')
t.bgcolor('dodger blue')
#t.speed('fast')
t.speed(0)

def rect(h, v, color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for counter in range(0,2):
        t.forward(h)
        t.right(90)
        t.forward(v)
        t.right(90)
    t.end_fill()
    t.penup()

def triangle(length, color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for c in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()
    t.penup()

#reverse the direction of the triangle from "left" to "right"
def triangle_reverse(length, color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for c in range(3):
        t.forward(length)
        t.right(120)
    t.end_fill()
    t.penup()

#origin (0,0)
#t.goto(0,0)
#rect(10,10,'white')

#ground covered with snow, with tree and snow mountain range (or a blue house with red roof later on)
#mountain range
t.goto(-300,-270)
rect(610,30,'white')

t.goto(-280,-270)
triangle(60,'white')

t.goto(-250,-270)
triangle(110,'white')

t.goto(-170,-270)
triangle(60,'white')

#trees
t.goto(243,-270)
triangle(60,'green')

t.goto(248,-240)
triangle(50,'green')

t.goto(253,-210)
triangle(40,'green')

t.goto(175,-270)
triangle(70,'green')

t.goto(180,-240)
triangle(60,'green')

t.goto(185,-210)
triangle(50,'green')

t.goto(120,-270)
triangle(60,'green')

t.goto(125,-240)
triangle(50,'green')

t.goto(130,-210)
triangle(40,'green')

#snowfall from the sky
for i in range (-300,325,100):
    for j in range (-230,440,100):
        t.goto(i,j)
        rect(10,10,'white')
        
#The rectangular snowfall is moving faster than the circular one (below)!
        
#        t.begin_fill()       
#        t.circle(5)
#        t.end_fill()

#Q.1 How to reverse the direction of propogation of snowball?
#Q.2 How to speed up the snowfall? Ans: t.speed(0), slower: 0 to 1 to 2 to 3

#left foot
t.goto(-85,-250)
rect(80,20,'black')

#right foot
t.goto(15,-250)
rect(80,20,'black')

#left leg
t.goto(-70,-100)
rect(50,150,'black')
t.goto(-70,-100)
rect(50,65,'red')

#right leg
t.goto(30,-100)
rect(50,150,'black')
t.goto(30,-100)
rect(50,65,'red')

#body with clothing
t.goto(-95,100)
rect(200,200,'red')

t.goto(-45,100)
triangle_reverse(100,'white')

#upper button (cancelled)
#t.goto(25,25)
#t.color('black')
#t.begin_fill()
#t.circle(7)
#t.end_fill()

#lower button (cancelled)
#t.goto(25,5)
#t.color('black')
#t.begin_fill()
#t.circle(7)
#t.end_fill()

t.goto(-5,60)
rect(20,160,'white')

#t.goto(-95,-10)
#rect(200,10,'white')

t.goto(-95,-92)
rect(200,23,'white')

#belt
t.goto(-95,-20)
rect(200,22,'black')
t.goto(-15,-20)
rect(40,23,'white')
t.goto(-11,-24)
rect(30,15,'black')
t.goto(-15,-29)
rect(17,5,'white')

#left arm
t.goto(-175,100)
rect(80,50,'red')

#right arm
t.goto(105,100)
rect(80,50,'red')

#left hand
t.goto(-195,210)
rect(40,160,'red')
t.goto(-195,200)
rect(40,20,'white')

t.goto(-175,210)
t.color('white')
t.begin_fill()
t.circle(25)
t.end_fill()

t.goto(-155,240)
t.color('white')
t.begin_fill()
t.circle(10)
t.end_fill()

#right hand
t.goto(165,210)
rect(40,160,'red')
t.goto(165,200)
rect(40,20,'white')

t.goto(185,210)
t.color('white')
t.begin_fill()
t.circle(25)
t.end_fill()

t.goto(165,240)
t.color('white')
t.begin_fill()
t.circle(10)
t.end_fill()

#neck (lacking a white scarf)
t.goto(-15,120)
rect(40,20,'bisque')

t.goto(-15,100)
triangle_reverse(40,'bisque')

#head (lacking a nose)
t.goto(-35,200)
rect(80,80,'bisque')
t.goto(-45,180)
rect(10,20,'bisque')
t.goto(45,180)
rect(10,20,'bisque')

#left eye
t.goto(-20,195)
rect(20,3, 'black')
t.goto(-20,185)
rect(20,10, 'white')
#t.goto(-15,175)
#rect(10,8, 'black')
t.goto(-10,175)
t.color('black')
t.begin_fill()
t.circle(5)
t.end_fill()

#right eye
t.goto(10,195)
rect(20,3,'black')
t.goto(10,185)
rect(20,10,'white')
#t.goto(15,175)
#rect(10,8,'black')
t.goto(20,175)
t.color('black')
t.begin_fill()
t.circle(5)
t.end_fill()

#mouth
t.goto(-20,155)
rect(50,6,'red')

#beard
t.goto(-25,140)
triangle_reverse(60,'white')

#hat
t.goto(-40,210)
rect(90,10,'white')

t.goto(-35,210)
triangle(80,'red')

t.goto(5,280)
t.color('white')
t.begin_fill()
t.circle(10)
t.end_fill()

#origin (0,0)
#t.goto(0,0)
#rect(10,10,'white')

t.hideturtle()
