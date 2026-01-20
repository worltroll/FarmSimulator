import arcade


class Carrot(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=1.8, **kwargs):
        super().__init__(path_or_texture='images/carrot.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class Beet(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=1.8, **kwargs):
        super().__init__(path_or_texture='images/beet.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class Potato(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=1.8, **kwargs):
        super().__init__(path_or_texture='images/potato.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class Backet(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.8, **kwargs):
        super().__init__(path_or_texture='images/backet.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)