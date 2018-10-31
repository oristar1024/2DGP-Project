from pico2d import *

MAP_WIDTH = 4000
MAP_HEGIHT = 3000

class Map:
    global MAP_HEGIHT, MAP_WIDTH
    def __init__(self):
        self.x, self.y = 25, 25
        self.number = 1
        self.image = load_image("Tiles.png")

    def draw(self):
        self.x, self.y = 25, 25
        while self.y < MAP_HEGIHT:
            while self.x < MAP_WIDTH:
                self.image.clip_draw((self.number - 1) * 65 + 2 + 5, 65 + 5, 50, 50, self.x, self.y)  # X값 + 2 는 파란선 부분제거용, X, Y 의+5는 테두리 자르기
                self.x += 50
            self.x = 25
            self.y += 50