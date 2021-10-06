from pico2d import *
def handle_events():
    global running
    global dir
    global ani
    global mouse_x, mouse_y
    events = get_events()
    for events in events:
        if events.type ==SDL_QUIT:
            running = False
        elif events.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = events.x, 600 - 1 - events.y
            if(mouse_x > 400):
                dir = 1
                ani = 1

            elif (mouse_x <= 400):
                dir = 1
                ani = 0


            elif events.key == SDLK_ESCAPE:
                running= False;
    pass
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')
running = True
frame = 0
dir = 0 # -1 left,+1 right
ani = 3 # 1오른쪽 0왼쪽
x, y = 800 // 2, 600 // 2
mouse_x = 500
mouse_y = 600//2
hide_cursor()
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * ani, 100, 100, x, y)
    mouse.clip_draw(0, 0, 50, 52, mouse_x, mouse_y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if (x<mouse_x):
        ani =1
        x += dir*5
    elif (x >= mouse_x):
        ani = 0
        x -= dir * 5
    if (y < mouse_y):
            y += dir * 5
    elif (y >= mouse_y):
            y -= dir * 5
    delay(0.01)
    
close_canvas()
