from pico2d import *

class Flatform:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 1600 // 2, 300
        self.cnt =0
        self.move_x = 0
    def update(self):
        self.move_x+= 1
        if self.cnt % 2 == 0:
            self.x += 1
        if self.cnt % 2 == 1:
            self.x -= 1
        self.x = clamp(25, self.x, 1600 - 25)
        if self.x == 1600 - 25:
            self.cnt += +1
        if self.x == 25:
            self.cnt += 1



    def draw(self):
        self.image.clip_draw(0,0,180,40,self.x,self.y)

        # fill here
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20
