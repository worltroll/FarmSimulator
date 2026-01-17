import random
import arcade

from pyglet.graphics import Batch


class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)


class StartView(arcade.View):
    TOMATO_COUNT = 10
    TOMATO_SPEED = 100

    BUTTON_OFFSET = 10

    def __init__(self, game_view):
        super().__init__()

        self.game_view = game_view

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.tomatoes = arcade.SpriteList()
        self.batch = Batch()

        for _ in range(self.TOMATO_COUNT):
            tomato = arcade.Sprite('images/tomato.png', scale=0.1)

            tomato.left = random.randint(0, int(self.window.width - tomato.width))
            tomato.bottom = random.randint(0, int(self.window.height - tomato.height))

            tomato.speed_y = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)
            while abs(tomato.speed_y) < 15:
                tomato.speed_y = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)

            tomato.speed_x = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)
            while abs(tomato.speed_x) < 15:
                tomato.speed_x = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)

            self.tomatoes.append(tomato)

        self.start_game_text = arcade.Text('Начать игру', self.window.width / 2, self.window.height / 8 * 4,
                                           batch=self.batch,
                                           anchor_x='center', anchor_y='center', font_size=17,
                                           font_name='Press Start 2P')
        self.start_game_rect = arcade.rect.XYWH(self.window.width / 2,
                                                self.window.height / 2,
                                                300, 100)
        self.start_game_color = arcade.color.YELLOW_ORANGE

        self.close_game_text = arcade.Text('Выйти', self.window.width / 2,
                                           self.window.height / 8 * 3 - self.BUTTON_OFFSET,
                                           batch=self.batch,
                                           anchor_x='center', anchor_y='center', font_size=17,
                                           font_name='Press Start 2P')
        self.close_game_rect = arcade.rect.XYWH(self.window.width / 2,
                                                self.window.height / 8 * 3 - self.BUTTON_OFFSET,
                                                300, 100)
        self.close_game_color = arcade.color.YELLOW_ORANGE

    def on_draw(self):
        self.clear()
        self.tomatoes.draw()
        arcade.draw.draw_rect_filled(self.start_game_rect, self.start_game_color)
        arcade.draw.draw_rect_outline(self.start_game_rect, arcade.color.BLACK, border_width=3)
        arcade.draw.draw_rect_filled(self.close_game_rect, self.close_game_color)
        arcade.draw.draw_rect_outline(self.close_game_rect, arcade.color.BLACK, border_width=3)
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
        if self.start_game_rect.left <= x <= self.start_game_rect.right and \
                self.start_game_rect.bottom <= y <= self.start_game_rect.top:
            self.window.show_view(self.game_view)

        if self.close_game_rect.left <= x <= self.close_game_rect.right and \
                self.close_game_rect.bottom <= y <= self.close_game_rect.top:
            self.window.close()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> bool | None:
        if self.start_game_rect.left <= x <= self.start_game_rect.right and \
                self.start_game_rect.bottom <= y <= self.start_game_rect.top:
            self.start_game_color = arcade.color.ORANGE_RED
        else:
            self.start_game_color = arcade.color.YELLOW_ORANGE

        if self.close_game_rect.left <= x <= self.close_game_rect.right and \
                self.close_game_rect.bottom <= y <= self.close_game_rect.top:
            self.close_game_color = arcade.color.ORANGE_RED
        else:
            self.close_game_color = arcade.color.YELLOW_ORANGE