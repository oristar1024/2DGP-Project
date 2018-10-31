from pico2d import *
import random
import main_state

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

class Monster:
    global character
    global SCREEN_WIDTH, SCREEN_HEIGHT
    def __init__(self):
        self.x, self.y = random.randint(0 + 50, SCREEN_WIDTH - 50), random.randint(0 + 50, SCREEN_HEIGHT - 50)
        self.hp = 100
        self.image = load_image('Dummy.png')
        self.box_x1 = self.x - 50
        self.box_x2 = self.x + 50
        self.box_y1 = self.y - 50
        self.box_y2 = self.y + 50
        self.hit = False
        self.hitchecker = 0

    def update(self):
        if self.hit and (self.hitchecker == main_state.character.idling_timer - 10 or self.hitchecker == main_state.character.idling_timer + 20):
            self.hit = False

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)