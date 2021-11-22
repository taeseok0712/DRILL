import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from flatform import Flatform


name = "MainState"

boy = None

def enter():
    global boy
    boy = Boy()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)

    global balls
    balls = [Ball() for i in range(10)]
    game_world.add_objects(balls, 1)

    global flatform

    flatform = Flatform()
    game_world.add_object(flatform,1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    global balls
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            balls.append(Ball())
            game_world.add_objects(balls, 1)
        else:
            boy.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # fill here
    global flatform



    for ball in balls:
        if collide(flatform, ball):
            ball.stop()
            ball.getflat(flatform.x)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()








