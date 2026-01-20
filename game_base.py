from GUI import HotBar, Field, Button

import arcade
from pyglet.graphics import Batch


class Game(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.batch = Batch()

        self.hotbar = HotBar()
        self.field = Field()
        self.exit_button = Button('images/button2.png', center_x=89, center_y=743, scale=0.5)
        self.exit_text = arcade.Text('Назад', 89, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.shop_button = Button('images/button2.png', center_x=473, center_y=743, scale=0.5)
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

        self.exit_button = Button('images/button2.png', center_x=89, center_y=743, scale=0.5)
        self.exit_text = arcade.Text('Назад', 89, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')

    def on_draw(self):
        self.clear()

        arcade.draw_sprite(self.exit_button)
        self.batch.draw()

    def on_mouse_press(self, x, y, dx, dy):
        if self.exit_button.left <= x <= self.exit_button.right and \
                self.exit_button.bottom <= y <= self.exit_button.top:
            self.window.show_view(self.game_view)