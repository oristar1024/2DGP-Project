from pico2d import *

MAP_WIDTH = 4000
MAP_HEGIHT = 3000
import main_state

class Map:
    global MAP_HEGIHT, MAP_WIDTH
    def __init__(self):
        self.image = load_image("Tiles.png")
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.window_left = 0
        self.window_bottom = 0
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0,0)

    def update(self):
        self.window_left = clamp(0, int(main_state.character.x) - self.canvas_width//2, self.w-self.canvas_width)
        self.window_bottom = clamp(0, int(main_state.character.y) - self.canvas_height//2, self.h - self.canvas_height)
