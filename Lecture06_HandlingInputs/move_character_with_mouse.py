from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x , y
    events =get_events()
    for events in events:
        if events.type == SDL_QUIT:
            running = False
        elif events.type ==SDL_MOUSEMOTION:
            x, y =events.x,KPU_HEIGHT -1 -events.y
        elif events.type == SDL_KEYDOWN and events.key == SDLK_ESCAPE:
            running = False;
    pass

open_canvas(KPU_WIDTH,KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




