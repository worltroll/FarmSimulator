import random
import arcade

from enum import Enum

from db_manager import DBManager
from sound_manager import *
from particle_manager import *

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
    VEGETABLE_COUNT = 5
    VEGETABLE_SPEED = 100

    BUTTON_OFFSET = 10
    SPRITES_PATHS = [
        'images/beet3.png',
        'images/carrot3.png',
        'images/potato3.png'
    ]

    def __init__(self, game_view):
        super().__init__()

        self.game_view = game_view
        self.level_select_mode = False
        self.emitters = []

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN

        self.vegetables = arcade.SpriteList()
        self.batch = Batch()

        for _ in range(self.VEGETABLE_COUNT):
            vegetable = arcade.Sprite(random.choice(self.SPRITES_PATHS), scale=0.5)
            attempts = 0
            max_attempts = 10000

            while attempts < max_attempts:
                vegetable.left = random.randint(0, int(self.window.width - vegetable.width))
                vegetable.bottom = random.randint(0, int(self.window.height - vegetable.height))

                safe_distance = vegetable.width * 2
                for other in self.vegetables:
                    if arcade.get_distance_between_sprites(vegetable, other) < safe_distance:
                        break
                else:
                    break
                attempts += 1

            if attempts == max_attempts:
                vegetable.center_x = self.window.width // 2
                vegetable.center_y = self.window.height // 2 + len(self.vegetables) * 150

            vegetable.speed_y = random.randint(-self.VEGETABLE_SPEED, self.VEGETABLE_SPEED)
            while abs(vegetable.speed_y) < 15:
                vegetable.speed_y = random.randint(-self.VEGETABLE_SPEED, self.VEGETABLE_SPEED)

            vegetable.speed_x = random.randint(-self.VEGETABLE_SPEED, self.VEGETABLE_SPEED)
            while abs(vegetable.speed_x) < 15:
                vegetable.speed_x = random.randint(-self.VEGETABLE_SPEED, self.VEGETABLE_SPEED)

            self.vegetables.append(vegetable)

        self.button_texture = arcade.load_texture('images/button_green.png')

        self.continue_game_text = arcade.Text('Продолжить игру', self.window.width / 2,
                                              self.window.height / 8 * 6 + self.BUTTON_OFFSET,
                                              batch=self.batch,
                                              anchor_x='center', anchor_y='center', font_size=12,
                                              font_name='Press Start 2P')
        self.continue_game_rect = arcade.rect.XYWH(self.window.width / 2,
                                                   self.window.height / 8 * 6 + self.BUTTON_OFFSET,
                                                   300, 100)
        self.continue_game_color = arcade.color.WHITE

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

        try:
            with open('save.json', 'r'):
                self.is_saved = True
        except Exception:
            self.is_saved = False

    def on_draw(self):
        self.clear()
        self.vegetables.draw()

        for e in self.emitters:
            e.draw()

        self.continue_game_text.text = 'Продолжить игру' if not self.level_select_mode and self.is_saved else ''
        self.start_game_text.text = 'Начать игру' if not self.level_select_mode else 'Легкий'
        self.close_game_text.text = 'Выйти' if not self.level_select_mode else 'Сложный'
        self.title_game_text.text = 'Титры' if not self.level_select_mode else 'Продвинутый'
        self.free_game_text.text = 'Таблица результатов' if not self.level_select_mode else 'Свободная игра'
        self.back_game_text.text = '' if not self.level_select_mode else 'Назад'

        self.continue_game_text.color = self.continue_game_color
        self.start_game_text.color = self.start_game_color
        self.close_game_text.color = self.close_game_color
        self.title_game_text.color = self.title_game_color
        self.free_game_text.color = self.free_game_color
        self.back_game_text.color = self.back_game_color

        arcade.draw_texture_rect(self.button_texture, self.start_game_rect)
        arcade.draw_texture_rect(self.button_texture, self.close_game_rect)
        arcade.draw_texture_rect(self.button_texture, self.title_game_rect)
        arcade.draw_texture_rect(self.button_texture, self.free_game_rect)

        if self.level_select_mode:
            arcade.draw_texture_rect(self.button_texture, self.back_game_rect)
        elif self.is_saved:
            arcade.draw_texture_rect(self.button_texture, self.continue_game_rect)
        self.batch.draw()

    def on_update(self, delta_time: float):
        for vegetable in self.vegetables:
            vegetable.center_x += vegetable.speed_x * delta_time
            vegetable.center_y += vegetable.speed_y * delta_time

            if vegetable.left < 0:
                vegetable.speed_x *= -1
                vegetable.left = 0

            if vegetable.right > self.width:
                vegetable.speed_x *= -1
                vegetable.right = self.width

            if vegetable.bottom < 0:
                vegetable.speed_y *= -1
                vegetable.bottom = 0

            if vegetable.top > self.height:
                vegetable.speed_y *= -1
                vegetable.top = self.height

            collided = arcade.check_for_collision_with_list(vegetable, self.vegetables)
            try:
                collided.remove(vegetable)
            except Exception:
                pass

            if collided:
                vegetable.speed_y *= -1
                vegetable.speed_x *= -1
                self.emitters.append(make_explosion(vegetable.center_x, vegetable.center_y))

        emitters_copy = self.emitters.copy()
        for e in emitters_copy:
            e.update(delta_time)
        for e in emitters_copy:
            if e.can_reap():
                self.emitters.remove(e)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.continue_game_rect.left <= x <= self.continue_game_rect.right and \
                self.continue_game_rect.bottom <= y <= self.continue_game_rect.top:
            if not self.level_select_mode and self.is_saved:
                self.window.show_view(self.game_view)
                self.game_view.difficulty = Difficulty.FREE_GAME
                self.game_view.setup()
                self.game_view.from_json()

        if self.start_game_rect.left <= x <= self.start_game_rect.right and \
                self.start_game_rect.bottom <= y <= self.start_game_rect.top:
            if not self.level_select_mode:
                self.level_select_mode = True
            else:
                self.game_view.difficulty = Difficulty.EASY
                self.game_view.setup()
                self.window.show_view(self.game_view)
                self.level_select_mode = False

        if self.title_game_rect.left <= x <= self.title_game_rect.right and \
                self.title_game_rect.bottom <= y <= self.title_game_rect.top:
            if not self.level_select_mode:
                self.window.show_view(self.titles)
            else:
                self.game_view.difficulty = Difficulty.ADVANCED
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

        if self.free_game_rect.left <= x <= self.free_game_rect.right and \
                self.free_game_rect.bottom <= y <= self.free_game_rect.top:
            if not self.level_select_mode:
                self.end_view.show_leaderboard = True
                self.window.show_view(self.end_view)
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
        if self.continue_game_rect.left <= x <= self.continue_game_rect.right and \
                self.continue_game_rect.bottom <= y <= self.continue_game_rect.top:
            self.continue_game_color = arcade.color.YELLOW_ORANGE
        else:
            self.continue_game_color = arcade.color.WHITE

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


class EndView(arcade.View):
    MAX_SYMBOLS = 10

    def __init__(self, db_manager: DBManager, start_view: StartView):
        super().__init__()

        self.db_manager = db_manager
        self.start_view = start_view
        self.difficulty_to_table = {
            Difficulty.EASY: 0,
            Difficulty.ADVANCED: 1,
            Difficulty.HARD: 2
        }
        arcade.set_background_color(arcade.color.TEA_GREEN)

    def setup(self):
        self.name_text_value = ''
        self.show_leaderboard = False
        self.difficulty = Difficulty.EASY
        self.leaderboard_index = 0
        self.everything = arcade.SpriteList()
        self.leaderboard_list = arcade.SpriteList()
        self.button_list = arcade.SpriteList()
        self.batch = Batch()
        self.leaderboard_batch = Batch()

        self.back_button = arcade.Sprite('images/button_gray.png', center_x=150, center_y=743)
        self.back_button.scale_x = 0.8
        self.back_button.scale_y = 0.5
        self.back_text = arcade.Text('Главное меню', 150, 743, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.button_list.append(self.back_button)

        self.easy_button = arcade.Sprite('images/button_brown.png', scale=0.5)
        self.easy_button.center_x = self.window.width / 4
        self.easy_button.bottom = 35
        self.leaderboard_list.append(self.easy_button)

        self.advanced_button = arcade.Sprite('images/button_brown.png', scale=0.5)
        self.advanced_button.center_x = self.window.width / 4 * 2
        self.advanced_button.bottom = 35
        self.leaderboard_list.append(self.advanced_button)

        self.hard_button = arcade.Sprite('images/button_brown.png', scale=0.5)
        self.hard_button.center_x = self.window.width / 4 * 3
        self.hard_button.bottom = 35
        self.leaderboard_list.append(self.hard_button)

        self.easy_button_text = arcade.Text(
            'Легко',
            self.easy_button.center_x,
            self.easy_button.center_y,
            anchor_x='center',
            anchor_y='center',
            font_size=12,
            font_name='Press Start 2P',
            color=arcade.color.WHITE
        )

        self.advanced_button_text = arcade.Text(
            'Средне',
            self.advanced_button.center_x,
            self.advanced_button.center_y,
            anchor_x='center',
            anchor_y='center',
            font_size=12,
            font_name='Press Start 2P',
            color=arcade.color.WHITE
        )

        self.hard_button_text = arcade.Text(
            'Сложно',
            self.hard_button.center_x,
            self.hard_button.center_y,
            anchor_x='center',
            anchor_y='center',
            font_size=12,
            font_name='Press Start 2P',
            color=arcade.color.WHITE
        )

        self.texture = arcade.load_texture('images/cell.png')
        self.rect = arcade.rect.XYWH(self.window.width / 2,
                                     self.window.height / 2,
                                     self.window.width / 8 * 7,
                                     self.window.height - 150)

        self.leaderboard_values = self.db_manager.get_leaderboard(self.leaderboard_index)

        self.leaderboard_text = arcade.Text('',
                                            self.window.width / 2,
                                            self.window.height - 150,
                                            width=self.window.width / 3 * 2,
                                            anchor_x='center',
                                            anchor_y='top',
                                            font_size=17,
                                            font_name='Press Start 2P',
                                            color=arcade.color.WHITE_SMOKE,
                                            batch=self.leaderboard_batch,
                                            multiline=True)

        self.text_field = arcade.Sprite('images/text_field.png')
        self.text_field.center_x = self.window.width / 2
        self.text_field.center_y = self.window.height / 2 + 100
        self.text_field.scale_x = 1.5
        self.text_field.scale_y = 0.8
        self.everything.append(self.text_field)

        self.name_text = arcade.Text(self.name_text_value,
                                     self.window.width / 2,
                                     self.window.height / 2 + 100,
                                     anchor_x='center',
                                     anchor_y='center',
                                     font_size=17,
                                     font_name='Press Start 2P',
                                     color=arcade.color.BLACK_OLIVE,
                                     batch=self.batch)

        self.instruction_text_holder = arcade.Sprite('images/button_gray.png')
        self.instruction_text_holder.center_x = self.window.width / 2
        self.instruction_text_holder.center_y = self.window.height / 2 - 100
        self.instruction_text_holder.scale_y = 1.5
        self.instruction_text_holder.scale_x = 1.8
        self.everything.append(self.instruction_text_holder)

        self.instruction_text = arcade.Text('Введите своё имя, затем перейдите к доске результатов нажав ENTER',
                                            self.window.width / 2,
                                            self.window.height / 2 - 100,
                                            width=self.window.width / 3 * 2,
                                            anchor_x='center',
                                            anchor_y='center',
                                            font_size=17,
                                            font_name='Press Start 2P',
                                            multiline=True,
                                            batch=self.batch)

        self.leaderboard_index = self.difficulty_to_table[self.difficulty]
        self.leaderboard_values = self.db_manager.get_leaderboard(self.leaderboard_index)
        text = ''
        for i, (name, score) in enumerate(self.leaderboard_values[:20]):
            line = f'{i + 1}.{" " * (3 - len(str(i + 1)))}{name}{" " * (self.MAX_SYMBOLS - len(name))}{score}\n'
            text += line
        self.leaderboard_text.text = text

    def on_draw(self) -> bool | None:
        self.clear()
        self.button_list.draw()
        self.back_text.draw()
        if not self.show_leaderboard:
            self.everything.draw()
            self.batch.draw()
        else:
            arcade.draw_texture_rect(self.texture, self.rect)
            self.leaderboard_batch.draw()
            self.leaderboard_list.draw()
            self.easy_button_text.draw()
            self.advanced_button_text.draw()
            self.hard_button_text.draw()

    def on_update(self, delta_time: float) -> bool | None:
        self.name_text.text = self.name_text_value

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        if len(self.name_text_value) <= self.MAX_SYMBOLS:
            if arcade.key.A <= symbol <= arcade.key.Z and not self.show_leaderboard:
                if not modifiers & arcade.key.MOD_SHIFT:
                    self.name_text_value += chr(symbol).lower()
                else:
                    self.name_text_value += chr(symbol).upper()

            elif symbol == arcade.key.SPACE:
                self.name_text_value += ' '

            elif arcade.key.KEY_0 <= symbol <= arcade.key.KEY_9:
                alternate_nums = '!@#$%^&*()'
                if not modifiers & arcade.key.MOD_SHIFT:
                    self.name_text_value += str(symbol - arcade.key.KEY_0)
                else:
                    self.name_text_value += alternate_nums[symbol - arcade.key.KEY_1]

        if symbol == arcade.key.BACKSPACE and self.name_text_value:
            self.name_text_value = self.name_text_value[:-1]

        if symbol == arcade.key.ENTER and self.name_text_value:
            self.show_leaderboard = True
            self.leaderboard_index = self.difficulty_to_table[self.difficulty]
            self.db_manager.add_new_score(self.leaderboard_index, self.name_text_value, self.score)
            self.leaderboard_values = self.db_manager.get_leaderboard(self.leaderboard_index)
            text = ''
            for i, (name, score) in enumerate(self.leaderboard_values[:20]):
                line = f"{i + 1}.{' ' * (3 - len(str(i + 1)))}{name}{' ' * (self.MAX_SYMBOLS - len(name))}{score}\n"
                text += line
            self.leaderboard_text.text = text

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> bool | None:
        if self.back_button in arcade.get_sprites_at_point((x, y), self.button_list):
            self.window.show_view(self.start_view)
            self.show_leaderboard = False
            self.name_text_value = ''

        if self.easy_button in arcade.get_sprites_at_point((x, y), self.leaderboard_list):
            self.difficulty = Difficulty.EASY
        elif self.advanced_button in arcade.get_sprites_at_point((x, y), self.leaderboard_list):
            self.difficulty = Difficulty.ADVANCED
        elif self.hard_button in arcade.get_sprites_at_point((x, y), self.leaderboard_list):
            self.difficulty = Difficulty.HARD

        self.leaderboard_index = self.difficulty_to_table[self.difficulty]
        self.leaderboard_values = self.db_manager.get_leaderboard(self.leaderboard_index)
        text = ''
        for i, (name, score) in enumerate(self.leaderboard_values[:20]):
            line = f'{i + 1}.{" " * (3 - len(str(i + 1)))}{name}{" " * (self.MAX_SYMBOLS - len(name))}{score}\n'
            text += line
        self.leaderboard_text.text = text


class Titles(arcade.View):
    TITLES_SPEED = 60
    MAX_SYMBOLS = 30

    def __init__(self, start_view: StartView):
        super().__init__()

        self.start_view = start_view
        self.emitters = []

        arcade.set_background_color(arcade.color.TEA_GREEN)

    def huge_boom(self, delta_time):
        for i in range(10):
            x, y = random.randint(0, self.window.width), random.randint(0, self.window.height)
            self.emitters.append(make_explosion(x, y))
            self.emitters.append(make_smoke_puff(x, y))

    def setup(self):
        self.y = self.height
        self.batch = Batch()
        self.button_list = arcade.SpriteList()

        with open('titles.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.texts = []
        x, y = self.window.width / 2, self.window.height
        for i, line in enumerate(lines):
            if len(line) > self.MAX_SYMBOLS:
                line = line[:self.MAX_SYMBOLS + 1]
            self.text = arcade.Text(
                line.strip(),
                x, y + 40 * i,
                anchor_x='center',
                anchor_y='center',
                batch=self.batch,
                font_name='Press Start 2P',
                font_size=12
            )
            self.texts.append(self.text)

        self.back_button = arcade.Sprite('images/button_gray.png', center_x=89, center_y=743, scale=0.5)
        self.back_text = arcade.Text('Назад', 89, 743, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.button_list.append(self.back_button)

    def on_draw(self) -> bool | None:

        self.clear()
        for e in self.emitters:
            e.draw()
        self.button_list.draw()
        self.batch.draw()
        self.back_text.draw()

    def on_update(self, delta_time: float) -> bool | None:
        for text in self.texts:
            text.y -= self.TITLES_SPEED * delta_time

        emitters_copy = self.emitters.copy()
        for e in emitters_copy:
            e.update(delta_time)
        for e in emitters_copy:
            if e.can_reap():
                self.emitters.remove(e)

    def on_show_view(self) -> None:
        arcade.schedule(self.huge_boom, 3)

    def on_hide_view(self) -> None:
        arcade.unschedule(self.huge_boom)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> bool | None:
        if self.back_button in arcade.get_sprites_at_point((x, y), self.button_list):
            self.window.show_view(self.start_view)
