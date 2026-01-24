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
        self.background_color = arcade.color.TEA_GREEN
        self.batch = Batch()

        self.hotbar = HotBar()
        self.field = Field()
        self.exit_button = Button('images/button_gray.png', center_x=89, center_y=743, scale=0.5)
        self.exit_text = arcade.Text('Назад', 89, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.shop_button = Button('images/button_gray.png', center_x=473, center_y=743, scale=0.5)
        self.shop_text = arcade.Text('Магазин', 473, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.coin_sign = arcade.Sprite('images/coin.png', center_x=344, center_y=743, scale=1.5)
        self.coin_text = arcade.Text('0', 281, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=20, font_name='Press Start 2P')

    def on_draw(self):
        self.clear()

        self.hotbar.draw()
        self.field.draw()
        arcade.draw_sprite(self.exit_button)
        arcade.draw_sprite(self.shop_button)
        arcade.draw_sprite(self.coin_sign)
        self.batch.draw()

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
        if self.exit_button.left <= x <= self.exit_button.right and \
                self.exit_button.bottom <= y <= self.exit_button.top:
            self.window.show_view(self.start_view)
        if self.shop_button.left <= x <= self.shop_button.right and \
                self.shop_button.bottom <= y <= self.shop_button.top:
            self.window.show_view(self.shop_view)


class Shop(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.batch = Batch()

        self.backet_cell = Cell('images/cell.png', 89, 622, item=Backet(89, 622))
        self.backet_text1 = arcade.Text('Ведро', 89, 510, batch=self.batch, anchor_x='center', anchor_y='center',
                                        font_size=12, font_name='Press Start 2P')
        self.backet_text2 = arcade.Text('с водой,', 89, 495, batch=self.batch, anchor_x='center', anchor_y='center',
                                        font_size=12, font_name='Press Start 2P')
        self.backet_text3 = arcade.Text('нужно', 89, 480, batch=self.batch, anchor_x='center', anchor_y='center',
                                        font_size=12, font_name='Press Start 2P')
        self.backet_text4 = arcade.Text('для полива', 89, 465, batch=self.batch, anchor_x='center', anchor_y='center',
                                        font_size=12, font_name='Press Start 2P')
        self.backet_text5 = arcade.Text('растений', 89, 450, batch=self.batch, anchor_x='center', anchor_y='center',
                                        font_size=12, font_name='Press Start 2P')

        self.money_cell = Cell('images/cell.png', 281, 622, item=None)
        self.money_text1 = arcade.Text('Улучшение', 281, 510, batch=self.batch, anchor_x='center', anchor_y='center',
                                       font_size=12, font_name='Press Start 2P')
        self.money_text2 = arcade.Text('+10%', 281, 495, batch=self.batch, anchor_x='center', anchor_y='center',
                                       font_size=12, font_name='Press Start 2P')
        self.money_text3 = arcade.Text('к прибыли', 281, 480, batch=self.batch, anchor_x='center', anchor_y='center',
                                       font_size=12, font_name='Press Start 2P')

        self.speed_cell = Cell('images/cell.png', 473, 622, item=None)
        self.speed_text1 = arcade.Text('Улучшение', 473, 510, batch=self.batch, anchor_x='center', anchor_y='center',
                                       font_size=12, font_name='Press Start 2P')
        self.speed_text2 = arcade.Text('+10%', 473, 495, batch=self.batch, anchor_x='center', anchor_y='center',
                                       font_size=12, font_name='Press Start 2P')
        self.speed_text3 = arcade.Text('к росту', 473, 480, batch=self.batch, anchor_x='center', anchor_y='center',
                                       font_size=12, font_name='Press Start 2P')
        self.speed_text4 = arcade.Text('овощей', 473, 465, batch=self.batch, anchor_x='center', anchor_y='center',
                                       font_size=12, font_name='Press Start 2P')

        self.packet_potato_cell = Cell('images/cell.png', 89, 267, item=PacketPotato(89, 267))
        self.packet_potato_text1 = arcade.Text('Семена', 89, 155, batch=self.batch, anchor_x='center',
                                               anchor_y='center', font_size=12, font_name='Press Start 2P')
        self.packet_potato_text2 = arcade.Text('картофеля', 89, 140, batch=self.batch, anchor_x='center',
                                               anchor_y='center', font_size=12, font_name='Press Start 2P')

        self.packet_carrot_cell = Cell('images/cell.png', 281, 267, item=PacketCarrot(281, 267))
        self.packet_carrot_text1 = arcade.Text('Семена', 281, 155, batch=self.batch, anchor_x='center',
                                               anchor_y='center', font_size=12, font_name='Press Start 2P')
        self.packet_carrot_text2 = arcade.Text('моркови', 281, 140, batch=self.batch, anchor_x='center',
                                               anchor_y='center', font_size=12, font_name='Press Start 2P')

        self.packet_beet_cell = Cell('images/cell.png', 473, 267, item=PacketBeet(473, 267))
        self.packet_beet_text1 = arcade.Text('Семена', 473, 155, batch=self.batch, anchor_x='center',
                                               anchor_y='center', font_size=12, font_name='Press Start 2P')
        self.packet_beet_text2 = arcade.Text('свеклы', 473, 140, batch=self.batch, anchor_x='center',
                                               anchor_y='center', font_size=12, font_name='Press Start 2P')

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
