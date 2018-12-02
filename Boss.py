from pico2d import *
import random
import main_state
from functions import *
import MonsterProjectile
import math
import game_framework
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

class Boss:
    global character
    global SCREEN_WIDTH, SCREEN_HEIGHT
    def __init__(self):
        self.x, self.y = random.randint(50, 3950), random.randint(150, 2750)
        self.hp = 2000 * game_framework.difficulty
        self.box_x1 = self.x - 75
        self.box_x2 = self.x + 75
        self.box_y1 = self.y - 75
        self.box_y2 = self.y + 75
        self.hit = False
        self.hitchecker = 0
        self.speed = 15
        self.frame = random.randint(0, 3)
        self.image = load_image('enemy_3.png')
        self.old_x = self.x
        self.old_y = self.y
        self.dir = 0
        self.move_x = 0
        self.move_y= 0
        self.mx, self.my = 0, 0
        self.dead = False
        self.attack_delay_checker = 0
        self.can_attack = True
        self.atk_rad =0
        self.type = 2

    def update(self):
        if self.hp <= 0:
            self.x, self.y = 0, 0
            self.dead = True
        else:
            self.old_x = self.x
            self.old_y = self.y
            if self.hit and self.hitchecker <= main_state.character.idling_timer - 0.8:
                self.hit = False
                self.frame = (self.frame + 1) % 4
            if get_dist(self.x, self.y, main_state.character.x, main_state.character.y) < 1000:
                self.move_x = (main_state.character.x - self.x) / get_dist(self.x, self.y, main_state.character.x, main_state.character.y)
                self.move_y = (main_state.character.y - self.y) / get_dist(self.x, self.y, main_state.character.x, main_state.character.y)
                if get_dist(self.x, self.y, main_state.character.x, main_state.character.y) < 300:
                    self.x -= self.move_x * self.speed
                    self.y -= self.move_y * self.speed
                else:
                    self.x += self.move_x * self.speed
                    self.y += self.move_y * self.speed
            if self.can_attack:
                for i in range(36):
                    main_state.monster_projectile[main_state.mp_array_index] = MonsterProjectile.MonsterProjectile(self)
                    main_state.monster_projectile[main_state.mp_array_index].move_x = math.cos(math.radians(i * 10 + self.atk_rad))
                    main_state.monster_projectile[main_state.mp_array_index].move_y = math.sin(math.radians(i * 10 + self.atk_rad))
                    main_state.monster_projectile[main_state.mp_array_index].damage = 20
                    main_state.mp_array_index = (main_state.mp_array_index + 1) % 1000
                self.can_attack = False
                self.atk_rad += 5
                self.attack_delay_checker = main_state.character.idling_timer

            if self.can_attack == False and self.attack_delay_checker <= main_state.character.idling_timer - 1:
                self.can_attack = True

            self.box_x1 = self.x - 75 - main_state.map.window_left
            self.box_x2 = self.x + 75 - main_state.map.window_bottom
            self.box_y1 = self.y - 75 - main_state.map.window_left
            self.box_y2 = self.y + 75 - main_state.map.window_bottom

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
        self.x = clamp(50, self.x, 3950)
        self.y = clamp(150, self.y, 2750)




    def draw(self):
        cx, cy = self.x - main_state.map.window_left, self.y - main_state.map.window_bottom
        if self.dead == False:
            self.image.clip_composite_draw(self.frame * 32, 96, 32, 32, 0, 'n', cx, cy, 150, 150)
