from GUI import HotBar, Field, Button

import arcade
from pyglet.graphics import Batch


class Game(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN

        self.hotbar = HotBar()
        self.field = Field()
        self.exit_button = Button('images/button2.png', center_x=89, center_y=743, scale=0.5)
        self.shop_button = Button('images/button2.png', center_x=473, center_y=743, scale=0.5)
        self.coin_sign = arcade.Sprite('images/coin.png', center_x=344, center_y=743, scale=1.5)
        self.batch = Batch()
        self.coin_text = arcade.Text('0', 218, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=17, font_name='Press Start 2P')

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
