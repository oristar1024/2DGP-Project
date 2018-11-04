from pico2d import *
import main_state
from functions import *
class Item:
    def __init__(self):
        self.image = load_image('item.png')
        self.type = 0
        self.x = 0
        self.y = 0
        self.comeup = False
    def update(self):
        if get_dist(self.x, self.y, main_state.character.x, main_state.character.y) < 50 and self.comeup:
            if self.type == 1:
                main_state.character.damage += main_state.character.item
            elif self.type == 2:
                main_state.character.hp += 100
            self.comeup = False

    def draw(self):
        if self.type == 1:
            self.image.clip_draw(0, 0, 68, 68, self.x, self.y)
        elif self.type == 2:
            self.image.clip_draw(68 * 2, 0, 68, 68, self.x, self.y)
