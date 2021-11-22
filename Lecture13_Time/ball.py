import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(500,799) , random.randint(Ball.MIN_FALL_SPEED,Ball.MAX_FALL_SPEED)



    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def stop(self):
        self.fall_speed = 0

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
    def getflat(self,x):
        self.x = x

    #fill here for def stop


# fill here
# class BigBall
class Bigball(Ball):

    image = None

    def __init__(self):
        if Bigball.image == None:
            Bigball.image = load_image('ball41x41.png')


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
class BigBall(Ball):
    MIN_FALL_SPEED = 50 # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200 # 200 pps = 6 meter per sec
    image = None
    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
            self.x, self.y = random.randint(0, 1600-1), 500
            self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED,
            BigBall.MAX_FALL_SPEED)
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
