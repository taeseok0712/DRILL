from pico2d import *
import random



KPU_WIDTH, KPU_HEIGHT = 1280, 1024

# 이 함수는 분석할 필요 없음. 기존 코드.
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

# 이 함수는 10개의 랜덤 위치의 화살표를 화면에 그려줌. 분석 필요 없음.
def draw_all_arrows():
    for i, p in enumerate(target_points):
        arrow.draw(p[0], p[1])
        pico2d.debug_font.draw(p[0], p[1], str(i), (255,0,0))



# 이 이후의 코드에 대한 분석하면 됨.


def update_character():
    global cx, cy
    global running_right
    global p1, p2, p3, p4
    global t
    global prev_cx
    #캐릭터의 x,y의 좌표를 곡선으로 이동시킴
    cx = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
    cy = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

    # 캐릭터의 위치가 목표 지점 (t가 1이됨)에 도달하면 다음 점을 설정해줌.
    t += 0.001
    if t >= 1.0:
        p1, p2, p3, p4 = get_next_four_points()
        t = 0


    # cx가 prev_cx보다 크면 오른쪽으로 가고 있는것이므로     running_right = cx > prev_cx 의 값을 true로 설정, 아닐시는 false로 설정함
    running_right = cx > prev_cx
    #prev_cx의 값을 cx로 생신해준다
    prev_cx = cx


# 아래 코드는 어떤 식으로 4개의 포인트를 가져오는가?
#시작지점을 현재 인덱스를 화살표의갯수(10)개의 나머지로 설정하고 , 끝지점을 시작지점의 +4로 설정
#이후 포인트를 시작 ~끝까지 4개로 설정후  현재 인덱스를 +1
def get_next_four_points():
    global cur_index
    start = cur_index % num_points
    end = start + 4
    points = extended_target_points[start:end]
    cur_index += 1
    return points

#설정한 크기로 캔버스를 연다
open_canvas(KPU_WIDTH, KPU_HEIGHT)

# prepare images
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
running_right = True
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
prev_cx = cx
frame = 0
hide_cursor()

num_points = 10
target_points = []
#타겟포인트(화살표의 좌표)를 설정해줌
for i in range(num_points):
    target_points.append((random.randint(100, KPU_WIDTH-100), random.randint(100, KPU_HEIGHT-100)))

# 아래의 코드에서, target_points[:3]을 더해서, extended_target_points를 만든 이유는?
# target_points[:3]을 더해주지 않으면 0~8번 화살표까진 이동하지만 , 9번 화살표로의 이동이 불가능 하기때문에 , 더해준것.

extended_target_points = target_points + target_points[:3]
cur_index = -1

t = 0
#p1, p2, p3, p4을 get_next_four_points()을 통해 업데이트 해준다
p1, p2, p3, p4 = get_next_four_points()

while running:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_all_arrows()
    if running_right:
        # 오른쪽을 보고있는 달리기 스프라이트로 그리기
        character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
    else:
        #왼쪽을 보고있는 달리기 스프라이트로 그리기
        character.clip_draw(frame * 100, 100 * 0, 100, 100, cx, cy)
    update_canvas()
    #애니메이션 효과를 넣기 위해 프레임을 업데이트 , 스프라이트 시트의 모션이 8개라 8의 나머지 계산을 해주면 , 값이 0~7로 설정됨
    frame = (frame + 1) % 8
    update_character()

    handle_events()

close_canvas()




