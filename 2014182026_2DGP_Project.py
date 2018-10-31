import game_framework
import pico2d

import main_state

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

pico2d.open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
game_framework.run(main_state)
pico2d.close_canvas()