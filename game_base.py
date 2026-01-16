from GUI import HotBar, Field

import arcade


class Game(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.hotbar = HotBar()
        self.field = Field()
        self.background_color = arcade.color.TEA_GREEN

    def on_draw(self):
        self.clear()

        self.hotbar.draw()
        self.field.draw()

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