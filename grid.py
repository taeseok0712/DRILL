import turtle

garo =5
sero =5
start_x= -350;
start_y=300;
turtle.penup()

turtle.goto(start_x,start_y)


turtle.pendown()

while(garo>=0):
    
    turtle.goto(start_x,start_y-500)
    garo -=1
    turtle.pendown()
    turtle.goto(start_x,start_y)
    start_x +=100
    turtle.penup()
  

start_x= -350;
start_y=300;


while(sero>=0):
    
    turtle.goto(start_x+500,start_y)
    sero -=1
    turtle.pendown()
    turtle.goto(start_x,start_y)
    start_y -=100
    turtle.penup()
