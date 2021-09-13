import turtle
import random

def turtle_move_W():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_move_D():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def turtle_move_A():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_move_S():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()
turtle.shape('turtle')

turtle.onkey(turtle_move_W,'w')
turtle.onkey(turtle_move_A,'a')
turtle.onkey(turtle_move_S,'s')
turtle.onkey(turtle_move_D,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
