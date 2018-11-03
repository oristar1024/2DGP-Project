from pico2d import *
import random
import main_state
from functions import *
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

class Monster:
    global character
    global SCREEN_WIDTH, SCREEN_HEIGHT
    def __init__(self):
        self.x, self.y = random.randint(100 + 50, SCREEN_WIDTH - 50), random.randint(100 + 50, SCREEN_HEIGHT - 50)
        self.hp = 100
        self.image = load_image('enemy_1.png')
        self.box_x1 = self.x - 25
        self.box_x2 = self.x + 25
        self.box_y1 = self.y - 25
        self.box_y2 = self.y + 25
        self.hit = False
        self.hitchecker = 0
        self.frame = 0
        self.type = 1
        self.old_x = self.x
        self.old_y = self.y
        self.dir = 0
        self.move_x = 0
        self.move_y= 0
        self.dead = False

    def update(self):
        if self.hp <= 0:
            self.x, self.y = 0, 0
            self.dead = True
        else:
            self.old_x = self.x
            self.old_y = self.y
            if self.hit and (self.hitchecker == main_state.character.idling_timer - 10 or self.hitchecker == main_state.character.idling_timer + 20):
                self.hit = False
            self.frame = (self.frame + 1) % 4
            if self.type == 1:
                if get_dist(self.x, self.y, main_state.character.x, main_state.character.y) < 1000 and get_dist(self.x, self.y, main_state.character.x, main_state.character.y) > 0:
                    self.move_x = (main_state.character.x - self.x) / get_dist(self.x, self.y, main_state.character.x, main_state.character.y)
                    self.move_y = (main_state.character.y - self.y) / get_dist(self.x, self.y, main_state.character.x, main_state.character.y)
                    self.x += self.move_x * 10
                    self.y += self.move_y * 10

            self.box_x1 = self.x - 25
            self.box_x2 = self.x + 25
            self.box_y1 = self.y - 25
            self.box_y2 = self.y + 25



    def draw(self):
        if self.type == 1 or self.type == 2:
            self.image.clip_draw(self.frame * 48, 0, 48, 48, self.x, self.y)