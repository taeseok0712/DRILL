from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x , y
    global ax, ay
    events =get_events()
    for events in events:
        if events.type == SDL_QUIT:
            running = False
        elif events.type ==SDL_MOUSEMOTION:
            ax, ay =events.x,KPU_HEIGHT -1 -events.y
        elif events.type == SDL_KEYDOWN and events.key == SDLK_ESCAPE:
            running = False;
    pass

def update_character():
    global x ,y
    global running_right
    if (x>ax):
        running_right =0
    if (x<ax):
        running_right =1

    x= (1-0.005)*x +0.005*ax
    y= (1-0.005)*y +0.005*ay

open_canvas(KPU_WIDTH,KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ax, ay = KPU_WIDTH // 2, KPU_HEIGHT // 2
running_right = 1
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * running_right, 100, 100, x, y)
    mouse.draw(ax,ay,50,52)
    update_canvas()
    frame = (frame + 1) % 8
    update_character()
    handle_events()

close_canvas()




