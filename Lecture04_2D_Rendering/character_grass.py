import math
from pico2d import *


open_canvas()

grass =load_image('grass.png')
character=load_image('character.png')


PosX =400
PosY =90
angle =0;

switch =False

while True:
    if switch ==True:
        if PosX>=0 and PosX<750 and PosY ==90:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(PosX,PosY)
            PosX+=5
            delay(0.01)
            if(PosX==400):
                switch =False

        elif PosX== 750 and PosY<600 and PosY >=90:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(PosX,PosY)
            PosY+=5
            delay(0.01)

        elif PosY== 600 and PosX>0 and PosX<=750:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(PosX,PosY)
            PosX-=5
            delay(0.01)
        elif PosX==0 and PosY>0 and PosY <=600:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(PosX,PosY)
            PosY-=5
            delay(0.01)
    if switch ==False:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400+ math.cos(-90+angle/360*2*math.pi) * 250,340+math.sin(-90+angle/360*2*math.pi) * 250)
            angle+=1;
            print(angle)
            if(angle==360):
                switch =True
                angle =0
