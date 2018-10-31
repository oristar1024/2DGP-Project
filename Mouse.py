from pico2d import *

class Mouse:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.image = load_image('Target.png')

    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)