# Introduction
import turtle
t=turtle.Turtle()
s=turtle.Screen()

def drawLine(t,x1,y1,x2,y2,c):
    t.color(c)
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)

drawLine(t,-100,100,-50,-100,"black")
drawLine(t,50,100,100,-100,"black")
drawLine(t,-200,50,200,50,"black")
drawLine(t,-200,-50,200,-50,"black")

print('your hashtag is done!')