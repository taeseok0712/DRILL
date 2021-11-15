from pico2d import *
import random
import game_world



class RunState:

    def enter(Bird, event):
        pass

    def exit(Bird, event):
        pass

    def do(Bird):
        Bird.frame = (Bird.frame + 1) % 14
        Bird.timer -= 1
        Bird.x += Bird.velocity
        Bird.x = clamp(25, Bird.x, 1600 - 25)

    def draw(Bird):
        if Bird.velocity == random.randint(1, 3):
            Bird.image.clip_draw(Bird.frame * 100, 100, 100, 100, Bird.x, Bird.y)
        else:
            Bird.image.clip_draw(Bird.frame * 100, 0, 100, 100, Bird.x, Bird.y)






class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100, 1000) ,  random.randint(130, 500)
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)


    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir)+ ' State' + self.cur_state.__name__)


