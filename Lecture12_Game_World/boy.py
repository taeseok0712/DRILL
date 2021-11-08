from pico2d import *
from ball import Ball
import game_world
# Boy Event
history = []
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER,SHIFT_DOWN , SHIFT_UP, DASH_TIMER ,DEBUG_KEY , SPACE = range(10)
eventName = ["RIGHT_DOWN", 'LEFT_DOWN', 'RIGHT_UP', 'LEFT_UP', 'SLEEP_TIMER','SHIFT_DOWN' ,'SHIFT_UP', 'DASH_TIMER','DEBUG_KEY','SPACE']
key_event_table = {

    (SDL_KEYDOWN, SDLK_d): DEBUG_KEY,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_RSHIFT): SHIFT_UP,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
}


# Boy States

class DashState:

    def enter(boy, event):
        print("enterDash")
        boy.dashTimer =100
        boy.dir = boy.velocity

    def exit(boy, event):
        print("exitDash")

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.dashTimer -= 1
        boy.x += boy.velocity *5
        boy.x = clamp(25, boy.x, 1600 - 25)
        if boy.dashTimer == 0:
            boy.add_event(DASH_TIMER)

    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

class IdleState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 1000

    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)



class RunState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)

    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState,SHIFT_UP: IdleState,SHIFT_DOWN: IdleState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState ,SHIFT_DOWN: DashState,SHIFT_UP: RunState, SPACE: RunState },
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState,SHIFT_UP: SleepState,SHIFT_DOWN: SleepState,SPACE: IdleState},
    DashState: {SHIFT_UP: RunState, DASH_TIMER: RunState,RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, SPACE: RunState }
}


class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)
    def fire_ball(self):
        ball = Ball(self.x, self.y - 25, self.dir * 3)
        game_world.add_object(ball, 1)
    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                history.append((self.cur_state.__name__, eventName[event]))
                self.cur_state = next_state_table[self.cur_state][event]
            except:

                print("curState:" , self.cur_state.__name__ , "event:", eventName[event])
                exit(-1)
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir)+ ' State' + self.cur_state.__name__)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]

            if(DEBUG_KEY == key_event):
                print(history[-4:])
            else:
                self.add_event(key_event)

