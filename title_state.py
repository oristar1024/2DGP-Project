import game_framework
from pico2d import *
import main_state

name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del(image)

import difficulty_state

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                game_framework.weapon = 1
                game_framework.change_state(difficulty_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                game_framework.weapon = 2
                game_framework.change_state(difficulty_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_3):
                game_framework.weapon = 3
                game_framework.change_state(difficulty_state)


def draw():
    clear_canvas()
    image.draw(1024/2, 768/2)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






