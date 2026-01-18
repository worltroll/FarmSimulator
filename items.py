import arcade


class Carrot(arcade.Sprite):
    def __init__(self, **kwargs):
        super().__init__(path_or_texture='images/carrot.png', **kwargs)


class Beet(arcade.Sprite):
    def __init__(self, **kwargs):
        super().__init__(path_or_texture='images/beet.png', **kwargs)


class Potato(arcade.Sprite):
    def __init__(self, **kwargs):
        super().__init__(path_or_texture='images/potato.png', **kwargs)