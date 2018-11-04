import game_framework
from pico2d import *


name = "DifficultyState"
image = None


def enter():
    global image
    image = load_image('difficulty.png')


def exit():
    global image
    del(image)

import main_state

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                game_framework.difficulty = 1
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                game_framework.difficulty = 2
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_3):
                game_framework.difficulty = 3
                game_framework.change_state(main_state)


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






