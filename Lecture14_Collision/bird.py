from pico2d import *
import random
import game_framework
import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 200.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


#사람크기의 1/3으로 설정함
#새의 평균 비행속도 200km







class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100, 1000) ,  random.randint(130, 500)
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0

        self.cnt = 0


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.velocity += RUN_SPEED_PPS
        if self.cnt %2 ==0:
            self.x += self.velocity * game_framework.frame_time
        if self.cnt % 2 == 1:
            self.x -= self.velocity * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)
        if self.x == 1600 - 25:
            self.cnt += +1
        if self.x == 25:
            self.cnt += 1
        print(self.x)
        self.dir = clamp(-1, self.velocity, 1)





    def draw(self):
        if self.velocity == 1:
            self.image.clip_draw(int(self.frame) * 100, 100, 500, 100, self.x, self.y ,33 ,33)
        else:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y,33,33)



