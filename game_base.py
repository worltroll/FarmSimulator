from GUI import *
from items import *
from base import Difficulty

import arcade
from pyglet.graphics import Batch


class Game(arcade.View):
    def __init__(self, default_difficulty: Difficulty):
        super().__init__()

        self.difficulty = default_difficulty

    def setup(self):
        self.pause_flag = False
        self.background_color = arcade.color.TEA_GREEN
        self.batch = Batch()

        self.hotbar = HotBar()
        self.field = Field()
        self.pause_button = Button('images/button_gray.png', center_x=89, center_y=743, scale=0.5)
        self.pause_text = arcade.Text('Пауза', 89, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.shop_button = Button('images/button_gray.png', center_x=473, center_y=743, scale=0.5)
        self.shop_text = arcade.Text('Магазин', 473, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.coin_sign = arcade.Sprite('images/coin.png', center_x=344, center_y=743, scale=1.5)
        self.coin_text = arcade.Text('0', 281, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=20, font_name='Press Start 2P')

        self.pause_batch = Batch()
        self.exit_button = Button('images/button_gray.png', center_x=281, center_y=500, scale=0.7)
        self.exit_text = arcade.Text('Выйти', 281, 500, batch=self.pause_batch, anchor_x='center', anchor_y='center',
                                      font_size=12, font_name='Press Start 2P')
        self.return_button = Button('images/button_gray.png', center_x=281, center_y=400, scale=0.7)
        self.return_text = arcade.Text('Вернуться', 281, 400, batch=self.pause_batch, anchor_x='center', anchor_y='center',
                                      font_size=12, font_name='Press Start 2P')
        self.again_button = Button('images/button_gray.png', center_x=281, center_y=300, scale=0.7)
        self.again_text = arcade.Text('Заново', 281, 300, batch=self.pause_batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')


    def on_draw(self):
        self.clear()

        self.hotbar.draw()
        self.field.draw()
        arcade.draw_sprite(self.pause_button)
        arcade.draw_sprite(self.shop_button)
        arcade.draw_sprite(self.coin_sign)
        self.batch.draw()

        if self.pause_flag:
            arcade.draw_sprite(self.exit_button)
            arcade.draw_sprite(self.return_button)
            arcade.draw_sprite(self.again_button)
            self.pause_batch.draw()

    def on_key_press(self, symbol, modifiers):
        match symbol:
            case arcade.key.KEY_1:
                self.hotbar.select(0)
            case arcade.key.KEY_2:
                self.hotbar.select(1)
            case arcade.key.KEY_3:
                self.hotbar.select(2)
            case arcade.key.KEY_4:
                self.hotbar.select(3)

    def on_mouse_press(self, x, y, dx, dy):
        if self.pause_button.left <= x <= self.pause_button.right and \
                self.pause_button.bottom <= y <= self.pause_button.top:
            self.pause_flag = True
        if self.shop_button.left <= x <= self.shop_button.right and \
                self.shop_button.bottom <= y <= self.shop_button.top:
            self.window.show_view(self.shop_view)

        if self.exit_button.left <= x <= self.exit_button.right and \
                self.exit_button.bottom <= y <= self.exit_button.top:
            self.window.show_view(self.end_view)
        if self.return_button.left <= x <= self.return_button.right and \
                self.return_button.bottom <= y <= self.return_button.top:
            self.pause_flag = False
        if self.again_button.left <= x <= self.again_button.right and \
                self.again_button.bottom <= y <= self.again_button.top:
            self.setup()


class Shop(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.batch = Batch()

        self.backet_cell = Cell('images/cell.png', 89, 622, item=Backet(89, 622))
        self.backet_text = arcade.Text('Ведро с водой, нужно для полива растений (1 монета)', 89, 490, batch=self.batch,
                                       anchor_x='center', anchor_y='center', font_size=12, font_name='Press Start 2P',
                                       width=128, multiline=True)

        self.money_cell = Cell('images/cell.png', 281, 622, item=None)
        self.money_text = arcade.Text('Улучшение +10% к прибыли (1 монета)', 281, 510, batch=self.batch,
                                      anchor_x='center', anchor_y='center', font_size=12, font_name='Press Start 2P',
                                      width=128, multiline=True)

        self.speed_cell = Cell('images/cell.png', 473, 622, item=None)
        self.speed_text = arcade.Text('Улучшение +10% к росту овощей (1 монета)', 473, 510, batch=self.batch,
                                      anchor_x='center',
                                      anchor_y='center', font_size=12, font_name='Press Start 2P', width=128,
                                      multiline=True)

        self.packet_potato_cell = Cell('images/cell.png', 89, 267, item=PacketPotato(89, 267))
        self.packet_potato_text = arcade.Text('Семена картофеля (1 монета)', 89, 155, batch=self.batch,
                                              anchor_x='center', anchor_y='center', font_size=12,
                                              font_name='Press Start 2P', width=128, multiline=True)

        self.packet_carrot_cell = Cell('images/cell.png', 281, 267, item=PacketCarrot(281, 267))
        self.packet_carrot_text = arcade.Text('Семена моркови (2 монеты)', 281, 155, batch=self.batch,
                                              anchor_x='center', anchor_y='center', font_size=12,
                                              font_name='Press Start 2P', width=128, multiline=True)

        self.packet_beet_cell = Cell('images/cell.png', 473, 267, item=PacketBeet(473, 267))
        self.packet_beet_text = arcade.Text('Семена свеклы (3 монеты)', 473, 155, batch=self.batch, anchor_x='center',
                                            anchor_y='center', font_size=12, font_name='Press Start 2P', width=128,
                                            multiline=True)

        self.exit_button = Button('images/button_gray.png', center_x=89, center_y=743, scale=0.5)
        self.exit_text = arcade.Text('Назад', 89, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')

    def on_draw(self):
        self.clear()

        self.backet_cell.draw()
        self.money_cell.draw()
        self.speed_cell.draw()
        self.packet_potato_cell.draw()
        self.packet_carrot_cell.draw()
        self.packet_beet_cell.draw()

        arcade.draw_sprite(self.exit_button)
        self.batch.draw()

    def on_mouse_press(self, x, y, dx, dy):
        if self.exit_button.left <= x <= self.exit_button.right and \
                self.exit_button.bottom <= y <= self.exit_button.top:
            self.window.show_view(self.game_view)
