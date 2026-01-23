import arcade


class Carrot(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/carrot.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class Beet(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/beet.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class Potato(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/potato.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class Backet(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/backet.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class PacketBeet(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/packet_beet.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class PacketCarrot(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/packet_carrot.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class PacketPotato(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/packet_potato.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)