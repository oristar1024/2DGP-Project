# 캐릭터 스프라이트의 머리는 4, 900 부터 X 40, Y 30 (글자위치 10)
# 몸통은 8, 850부터 X32, Y30, 머리로부터 Y를 15만큼 빼준다.
# 맵타일은 한칸에 X, Y 각 65
from pico2d import *
import Character
import CharacterProjectile
import Monster
import Mouse
import Map
import Item
import Boss

hide_cursor()
character_projectile = [None for i in range(30)]
monster_projectile = [None for i in range(1000)]
mp_array_index = 0
projectile_array_index = 0
character = None
mouse = None
map = None
monsters = None
kill_counter = 0
items = [None, None]
clear = False
boss_comeup = 0
boss = None

def enter():
    global character, mouse, map, monsters
    global items
    character = Character.Character()
    mouse = Mouse.Mouse()
    map = Map.Map()
    monsters = [Monster.Monster() for i in range(60)]
    items = [Item.Item() for i in range(2)]

def exit():
    pass

def update():
    global character, monsters
    global character_projectile
    global kill_counter
    global clear
    global boss_comeup
    global boss
    global map

    character.update()
    map.update()
    for i in range(30):
        if character_projectile[i] != None:
            character_projectile[i].update()
            if character_projectile[i].delete:
                character_projectile[i] = None
    for i in range(1000):
        if monster_projectile[i] != None:
            monster_projectile[i].update()
            if monster_projectile[i].delete:
                monster_projectile[i] = None

    kill_counter = 0
    if clear == False:
        for monster in monsters:
            if monster.dead == False:
                monster.update()
            else:
                kill_counter += 1
        if kill_counter == 60:
            for item in items:
                item.comeup = True
                items[0].x = 1900 - map.window_left
                items[0].y = 1500 - map.window_bottom
                items[0].type = 1
                items[1].x = 2100 - map.window_left
                items[1].y = 1500 - map.window_bottom
                items[1].type = 2
            clear = True

    for item in items:
        if item.comeup:
            item.update()

    if boss_comeup == 2:
        boss = Boss.Boss()
        boss_comeup += 1

    if boss_comeup == 3:
        boss.update()



def draw():
    global character, monsters
    global character_projectile
    global items
    global boss_comeup
    global boss
    clear_canvas()
    map.draw()

    for monster in monsters:
        if monster.dead == False:
            monster.draw()

    for projectile in character_projectile:
        if projectile != None:
            projectile.draw()

    for projectile in monster_projectile:
        if projectile != None:
            projectile.draw()

    for item in items:
        if item.comeup:
            item.draw()

    if boss_comeup == 3:
        boss.draw()

    character.draw()
    mouse.draw()
    update_canvas()
    delay(0.01)

def handle_events():
    global running
    global character
    global mouse
    global character_projectile
    global projectile_array_index
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_w:
                character.up_move = True

            elif event.key == SDLK_a:
                character.left_move = True

            elif event.key == SDLK_d:
                character.right_move = True

            elif event.key == SDLK_s:
                character.down_move = True

            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_t:
                for monster in monsters:
                    monster.dead = True
        elif event.type == SDL_MOUSEMOTION:
            mouse.x, mouse.y = event.x, 768 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and character.can_attack:
            character_projectile[projectile_array_index] = CharacterProjectile.CharacterProjectile()
            projectile_array_index = (projectile_array_index + 1) % 30
            character.can_attack = False
            character.attack_delay_checker = character.idling_timer

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                character.up_move = False

            elif event.key == SDLK_a:
                character.left_move = False

            elif event.key == SDLK_d:
                character.right_move = False

            elif event.key == SDLK_s:
                character.down_move = False

def pause():
    pass

def resume():
    pass
