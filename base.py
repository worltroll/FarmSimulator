import random
import arcade

from enum import Enum

from pyglet.graphics import Batch


class Difficulty(Enum):
    EASY = 'easy'
    ADVANCED = 'advanced'
    HARD = 'hard'
    FREE_GAME = 'free_game'


class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)
        self.coins = 0


class StartView(arcade.View):
    TOMATO_COUNT = 10
    TOMATO_SPEED = 100

    BUTTON_OFFSET = 10
    SPRITES_PATHS = [
        'images/beet.png',
        'images/carrot.png',
        'images/potato.png'
    ]

    def __init__(self, game_view):
        super().__init__()

        self.game_view = game_view
        self.level_select_mode = False

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN

        self.vegetables = arcade.SpriteList()
        self.batch = Batch()

        for _ in range(self.TOMATO_COUNT):
            vegetable = arcade.Sprite(random.choice(self.SPRITES_PATHS), scale=0.5)

            vegetable.left = random.randint(0, int(self.window.width - vegetable.width))
            vegetable.bottom = random.randint(0, int(self.window.height - vegetable.height))

            vegetable.speed_y = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)
            while abs(vegetable.speed_y) < 15:
                vegetable.speed_y = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)

            vegetable.speed_x = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)
            while abs(vegetable.speed_x) < 15:
                vegetable.speed_x = random.randint(-self.TOMATO_SPEED, self.TOMATO_SPEED)

            self.vegetables.append(vegetable)

        self.button_texture = arcade.load_texture('images/button_green.png')

        self.start_game_text = arcade.Text('Начать игру', self.window.width / 2, self.window.height / 8 * 5,
                                           batch=self.batch,
                                           anchor_x='center', anchor_y='center', font_size=12,
                                           font_name='Press Start 2P')
        self.start_game_rect = arcade.rect.XYWH(self.window.width / 2,
                                                self.window.height / 8 * 5,
                                                300, 100)
        self.start_game_color = arcade.color.WHITE

        self.title_game_text = arcade.Text('Титры', self.window.width / 2,
                                           self.window.height / 8 * 4 - self.BUTTON_OFFSET,
                                           batch=self.batch,
                                           anchor_x='center', anchor_y='center', font_size=12,
                                           font_name='Press Start 2P')
        self.title_game_rect = arcade.rect.XYWH(self.window.width / 2,
                                                self.window.height / 8 * 4 - self.BUTTON_OFFSET,
                                                300, 100)
        self.title_game_color = arcade.color.WHITE

        self.close_game_text = arcade.Text('Выйти', self.window.width / 2,
                                           self.window.height / 8 * 3 - self.BUTTON_OFFSET * 2,
                                           batch=self.batch,
                                           anchor_x='center', anchor_y='center', font_size=12,
                                           font_name='Press Start 2P')
        self.close_game_rect = arcade.rect.XYWH(self.window.width / 2,
                                                self.window.height / 8 * 3 - self.BUTTON_OFFSET * 2,
                                                300, 100)
        self.close_game_color = arcade.color.WHITE

        self.free_game_text = arcade.Text('', self.window.width / 2,
                                          self.window.height / 8 * 2 - self.BUTTON_OFFSET * 3,
                                          batch=self.batch,
                                          anchor_x='center', anchor_y='center', font_size=12,
                                          font_name='Press Start 2P')
        self.free_game_rect = arcade.rect.XYWH(self.window.width / 2,
                                               self.window.height / 8 * 2 - self.BUTTON_OFFSET * 3,
                                               300, 100)
        self.free_game_color = arcade.color.WHITE

        self.back_game_text = arcade.Text('', 89, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                          font_size=12, font_name='Press Start 2P')
        self.back_game_rect = arcade.rect.LBWH(25, 711, 128, 64)
        self.back_game_color = arcade.color.WHITE

    def on_draw(self):
        self.clear()
        self.vegetables.draw()

        self.start_game_text.text = 'Начать игру' if not self.level_select_mode else 'Легкий'
        self.close_game_text.text = 'Выйти' if not self.level_select_mode else 'Сложный'
        self.title_game_text.text = 'Титры' if not self.level_select_mode else 'Продвинутый'
        self.free_game_text.text = '' if not self.level_select_mode else 'Свободная игра'
        self.back_game_text.text = '' if not self.level_select_mode else 'Назад'

        self.start_game_text.color = self.start_game_color
        self.close_game_text.color = self.close_game_color
        self.title_game_text.color = self.title_game_color
        self.free_game_text.color = self.free_game_color
        self.back_game_text.color = self.back_game_color

        arcade.draw_texture_rect(self.button_texture, self.start_game_rect)
        arcade.draw_texture_rect(self.button_texture, self.close_game_rect)
        arcade.draw_texture_rect(self.button_texture, self.title_game_rect)
        if self.level_select_mode:
            arcade.draw_texture_rect(self.button_texture, self.free_game_rect)
            arcade.draw_texture_rect(self.button_texture, self.back_game_rect)
        self.batch.draw()

    def on_update(self, delta_time: float):
        for tomato in self.vegetables:
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

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.start_game_rect.left <= x <= self.start_game_rect.right and \
                self.start_game_rect.bottom <= y <= self.start_game_rect.top:
            if not self.level_select_mode:
                self.level_select_mode = True
            else:
                self.game_view.difficulty = Difficulty.EASY
                self.game_view.setup()
                self.window.show_view(self.game_view)
                self.level_select_mode = False

        if self.close_game_rect.left <= x <= self.close_game_rect.right and \
                self.close_game_rect.bottom <= y <= self.close_game_rect.top:
            if not self.level_select_mode:
                self.window.close()
            else:
                self.game_view.difficulty = Difficulty.HARD
                self.game_view.setup()
                self.window.show_view(self.game_view)
                self.level_select_mode = False

        if self.title_game_rect.left <= x <= self.title_game_rect.right and \
                self.title_game_rect.bottom <= y <= self.title_game_rect.top:
            if not self.level_select_mode:
                print('ТИТРЫ')
            else:
                self.game_view.difficulty = Difficulty.ADVANCED
                self.game_view.setup()
                self.window.show_view(self.game_view)
                self.level_select_mode = False

        if self.free_game_rect.left <= x <= self.free_game_rect.right and \
                self.free_game_rect.bottom <= y <= self.free_game_rect.top:
            if not self.level_select_mode:
                return
            else:
                self.game_view.difficulty = Difficulty.FREE_GAME
                self.game_view.setup()
                self.window.show_view(self.game_view)
                self.level_select_mode = False

        if self.back_game_rect.left <= x <= self.back_game_rect.right and \
                self.back_game_rect.bottom <= y <= self.back_game_rect.top:
            if self.level_select_mode:
                self.level_select_mode = False

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> bool | None:
        if self.start_game_rect.left <= x <= self.start_game_rect.right and \
                self.start_game_rect.bottom <= y <= self.start_game_rect.top:
            self.start_game_color = arcade.color.YELLOW_ORANGE
        else:
            self.start_game_color = arcade.color.WHITE

        if self.close_game_rect.left <= x <= self.close_game_rect.right and \
                self.close_game_rect.bottom <= y <= self.close_game_rect.top:
            self.close_game_color = arcade.color.YELLOW_ORANGE
        else:
            self.close_game_color = arcade.color.WHITE

        if self.title_game_rect.left <= x <= self.title_game_rect.right and \
                self.title_game_rect.bottom <= y <= self.title_game_rect.top:
            self.title_game_color = arcade.color.YELLOW_ORANGE
        else:
            self.title_game_color = arcade.color.WHITE

        if self.free_game_rect.left <= x <= self.free_game_rect.right and \
                self.free_game_rect.bottom <= y <= self.free_game_rect.top:
            self.free_game_color = arcade.color.YELLOW_ORANGE
        else:
            self.free_game_color = arcade.color.WHITE

        if self.back_game_rect.left <= x <= self.back_game_rect.right and \
                self.back_game_rect.bottom <= y <= self.back_game_rect.top:
            self.back_game_color = arcade.color.YELLOW_ORANGE
        else:
            self.back_game_color = arcade.color.WHITE