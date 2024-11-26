from pico2d import *
import game_world
import game_framework
import random
import server


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

        self.cw = get_canvas_width()
        self.ch = get_canvas_height()

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):

        self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, int(server.background.w) - self.cw - 1)
        self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, int(server.background.h) - self.ch - 1)

        if self.window_left != 0 and self.window_left != int(server.background.w) - self.cw - 1:
            self.x -= math.cos(server.boy.dir) * server.boy.speed * game_framework.frame_time  # 타일 이동에 맞춰 x 좌표 수정

        if self.window_bottom != 0 and self.window_bottom != int(server.background.h) - self.ch - 1:
            self.y -= math.sin(server.boy.dir) * server.boy.speed * game_framework.frame_time

        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)
        pass
