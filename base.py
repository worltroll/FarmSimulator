import random
import arcade

from pyglet.graphics import Batch

from game_base import Game


class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)


class StartView(arcade.View):
    TOMATO_COUNT = 10
    TOMATO_SPEED = 100

    def __init__(self, game_view):
        super().__init__()

        self.game_view = game_view

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.tomatoes = arcade.SpriteList()
        self.batch = Batch()

        for _ in range(self.TOMATO_COUNT):
            tomato = arcade.Sprite('images/tomato.png', scale=0.1,
                                   center_x=random.randint(0, self.window.width - 30),
                                   center_y=random.randint(0, self.window.height - 30))

            tomato.speed_y = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)
            tomato.speed_x = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)

            self.tomatoes.append(tomato)

        self.start_game_text = arcade.Text('Начать игру', self.window.width / 2, self.window.height / 2,
                                           batch=self.batch,
                                           anchor_x='center', anchor_y='center')
        self.start_game_rect = arcade.rect.XYWH(self.window.width / 2,
                                                self.window.height / 2,
                                                200, 100)

    def on_draw(self):
        self.clear()
        self.tomatoes.draw()
        arcade.draw.draw_rect_filled(self.start_game_rect, arcade.color.YELLOW_ORANGE)
        self.batch.draw()

    def on_update(self, delta_time: float):
        for tomato in self.tomatoes:
            tomato.center_x += tomato.speed_x * delta_time
            tomato.center_y += tomato.speed_y * delta_time

            if tomato.left < 0:
                tomato.speed_x *= -1
                tomato.left = 0

            if tomato.right > self.width:
                tomato.speed_x *= -1
                tomato.right = self.width

            if tomato.bottom < 0:
                tomato.speed_y *= -1
                tomato.bottom = 0

            if tomato.top > self.height:
                tomato.speed_y *= -1
                tomato.top = self.height

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> bool | None:
        is_clicked = False
        if self.start_game_rect.left <= x <= self.start_game_rect.right:
            if self.start_game_rect.bottom <= y <= self.start_game_rect.top:
                is_clicked = True