from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0


def handle_events():
    global running
    events = get_events()
    for events in events:
        if events.type == SDL_QUIT:
            running = False
        if events.type == SDL_KEYDOWN and events.key == SDLK_ESCAPE:
            running = False
    pass


while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 1
    delay(0.01)

close_canvas()

