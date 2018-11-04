from pico2d import *
from functions import *
import main_state

class MonsterProjectile:
    image = None
    def __init__(self, monster):
        if MonsterProjectile.image == None:
            MonsterProjectile.image = load_image('monsterprojectile.png')
        self.x = monster.x
        self.y = monster.y
        self.move_count = 40
        self.i = 0
        self.delete = False
        if monster.type == 1:
            self.target_x = main_state.character.x
            self.target_y = main_state.character.y
            self.move_y = (self.target_y - self.y) / get_dist(self.x, self.y, self.target_x, self.target_y)
            self.move_x = (self.target_x - self.x) / get_dist(self.x, self.y, self.target_x, self.target_y)
        self.old_x, self.old_y = self.x, self.y

    def update(self):
        global character_projectile
        if self.i < self.move_count and self.delete == False:
            self.old_x, self.old_y = self.x, self.y
            self.x += self.move_x * 20
            self.y += self.move_y * 20
            self.i += 1
        else:
            self.delete = True

        if main_state.character.hit == False and crush_check_line(self.old_x, self.old_y, self.x + self.move_x * 30, self.y + self.move_y * 30 , main_state.character.x - 25, main_state.character.y -25, main_state.character.x +25, main_state.character.y +25):
            main_state.character.hit = True
            main_state.character.hp -= 10
            main_state.character.hitchecker = main_state.character.idling_timer
            self.delete = True




    def draw(self):
        self.image.clip_draw(0,0,15,15,self.x,self.y)
