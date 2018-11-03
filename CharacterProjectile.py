from pico2d import *
from functions import *
import main_state

class CharacterProjectile:
    image = None
    def __init__(self):
        if CharacterProjectile.image == None:
            CharacterProjectile.image = load_image('projectile.png')
        self.x = main_state.character.x
        self.y = main_state.character.y
        self.target_x = main_state.mouse.x
        self.target_y = main_state.mouse.y
        self.move_y = (self.target_y - self.y) / get_dist(self.x, self.y, self.target_x, self.target_y)
        self.move_x = (self.target_x - self.x) / get_dist(self.x, self.y, self.target_x, self.target_y)
        self.rad = math.acos(self.move_x)
        self.move_count = main_state.character.range / main_state.character.bullet_speed
        self.i = 0
        self.delete = False
        self.old_x, self.old_y = self.x, self.y
        self.frame = 0
        self.bomb = False
        if self.y > self.target_y:
            self.rad = -self.rad

    def update(self):
        global character_projectile
        if self.i < self.move_count and self.bomb == False:
            self.old_x, self.old_y = self.x, self.y
            self.x += self.move_x * main_state.character.bullet_speed
            self.y += self.move_y * main_state.character.bullet_speed
            self.i += 1
            if main_state.character.weapon == 1:
                self.frame = (self.frame + 1) % 3
            elif main_state.character.weapon == 2:
                self.frame = (self.frame + 1) % 2
            elif main_state.character.weapon == 3:
                self.frame = (self.frame + 1) % 4
        else:
            if main_state.character.weapon != 3:
                self.delete = True
            elif main_state.character.weapon == 3:
                if self.frame == 5:
                    for monster in main_state.monsters:
                        if monster.hp > 0 and get_dist(self.x, self.y, monster.x, monster.y) <= main_state.character.bomb_range:
                            monster.hp -= main_state.character.damage
                elif self.frame == 7:
                    self.delete = True
                self.bomb = True
                self.frame = (self.frame + 1) % 8
                self.x += self.move_x * 15
                self.y += self.move_y * 15

        for monster in main_state.monsters:
            if monster.hit == False and monster.hp > 0 and crush_check_line(self.old_x, self.old_y, self.x + self.move_x * 45, self.y + self.move_y * 25, monster.box_x1, monster.box_y1, monster.box_x2, monster.box_y2):
                if main_state.character.weapon == 3:
                    self.bomb = True
                elif main_state.character.weapon != 3:
                    monster.hp -= main_state.character.damage
                    if main_state.character.weapon == 1:
                        self.delete = True
                        break
                    if main_state.character.weapon == 2:
                        monster.hit = True
                        monster.hitchecker = main_state.character.idling_timer



    def draw(self):
        if main_state.character.weapon == 1:
            self.image.clip_composite_draw(0 + 90 * self.frame, 200, 90, 50, self.rad + 3.14, 'n', self.x, self.y, 90, 50)
        elif main_state.character.weapon == 2:
            self.image.clip_composite_draw(0 + 90 * self.frame, 450, 90, 50, self.rad + 3.14, 'n', self.x, self.y, 90, 50)
        if main_state.character.weapon == 3:
            self.image.clip_composite_draw(0 + 90 * self.frame, 1200, 90, 150, self.rad + 3.14, 'n', self.x, self.y, 90, 150)
