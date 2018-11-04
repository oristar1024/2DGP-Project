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
        self.box_x1 = self.x - 25
        self.box_x2 = self.x + 25
        self.box_y1 = self.y - 25
        self.box_y2 = self.y + 25
        self.hit = False
        self.hitchecker = 0
        self.frame = 0
        self.type = random.randint(0, 1)
        if self.type == 0:
            self.image = load_image('enemy_1.png')
        elif self.type == 1:
            self.image = load_image('enemy_2.png')
        self.old_x = self.x
        self.old_y = self.y
        self.dir = 0
        self.move_x = 0
        self.move_y= 0
        self.mx, self.my = 0, 0
        self.dead = False

    def update(self):
        if self.hp <= 0:
            self.x, self.y = 0, 0
            self.dead = True
        else:
            self.old_x = self.x
            self.old_y = self.y
            if self.hit and self.hitchecker <= main_state.character.idling_timer - 0.8:
                self.hit = False
            if self.type == 0:
                self.frame = (self.frame + 1) % 4
            elif self.type == 1:
                self.frame = (self.frame + 1) % 3
            if self.type == 0:
                if get_dist(self.x, self.y, main_state.character.x, main_state.character.y) < 1000 and get_dist(self.x, self.y, main_state.character.x, main_state.character.y) > 0:
                    self.move_x = (main_state.character.x - self.x) / get_dist(self.x, self.y, main_state.character.x, main_state.character.y)
                    self.move_y = (main_state.character.y - self.y) / get_dist(self.x, self.y, main_state.character.x, main_state.character.y)
                    self.x += self.move_x * 10
                    self.y += self.move_y * 10
            if self.type == 1:
                if get_dist(self.x, self.y, main_state.character.x, main_state.character.y) < 1200:
                    self.move_x = (main_state.character.x - self.x) / get_dist(self.x, self.y, main_state.character.x, main_state.character.y)
                    self.move_y = (main_state.character.y - self.y) / get_dist(self.x, self.y, main_state.character.x, main_state.character.y)
                    if get_dist(self.x, self.y, main_state.character.x, main_state.character.y) < 500:
                        self.x -= self.move_x * 10
                        self.y -= self.move_y * 10
                    else:
                        self.x += self.move_x * 10
                        self.y += self.move_y * 10

            self.box_x1 = self.x - 25
            self.box_x2 = self.x + 25
            self.box_y1 = self.y - 25
            self.box_y2 = self.y + 25

            if self.move_x < 0:
                self.mx = -self.move_x
            else:
                self.mx = self.move_x
            if self.move_y < 0:
                self.my = -self.move_y
            else:
                self.my = self.move_y

            if self.mx >= self.my:
                if self.move_x < 0 :
                    self.dir = 3
                else:
                    self.dir = 0
            else:
                if self.move_y < 0:
                    self.dir = 2
                else:
                    self.dir = 1




    def draw(self):
        if self.type == 0:
            if self.dir == 0 or self.dir == 1 or self.dir == 2:
                self.image.clip_draw(self.frame * 48, self.dir * 48, 48, 48, self.x, self.y)
            else:
                self.image.clip_composite_draw(self.frame * 48, 0, 48, 48, 0, 'h', self.x, self.y, 48, 48)
        if self.type == 1:
            if self.dir == 0 or self.dir == 2:
                self.image.clip_draw(48 * 6 + self.frame * 48, 96, 48, 48, self.x, self.y)
            elif self.dir == 1:
                self.image.clip_draw(48 * 6 + self.frame * 48, 48, 48, 48, self.x, self.y)
            else:
                self.image.clip_composite_draw(48 * 6 + self.frame * 48, 96, 48, 48, 0, 'h', self.x, self.y, 48, 48)