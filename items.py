import arcade


class Potato(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/potato0.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)
        self.money = 3  # 1 - стоимость, 1 - вода, 1 - доход
        self.time = 0
        self.index = 0
        self.interaction_flag = False

    def update_animation(self, delta_time, animation_time):
        self.time += delta_time
        if self.time >= animation_time / 4 and self.index < 3:
            self.time = 0
            self.index += 1
            self.texture = arcade.load_texture(
                ['images/potato0.png', 'images/potato1.png', 'images/potato2.png', 'images/potato3.png'][self.index])
        if self.index == 3:
            self.interaction_flag = True


class Carrot(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/carrot0.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)
        self.money = 5  # 2 - стоимость, 1 - вода, 2 - доход
        self.time = 0
        self.index = 0
        self.interaction_flag = False

    def update_animation(self, delta_time, animation_time):
        self.time += delta_time
        if self.time >= animation_time / 4 and self.index < 3:
            self.time = 0
            self.index += 1
            self.texture = arcade.load_texture(
                ['images/carrot0.png', 'images/carrot1.png', 'images/carrot2.png', 'images/carrot3.png'][self.index])
        if self.index == 3:
            self.interaction_flag = True


class Beet(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/beet0.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)
        self.money = 8  # 3 - стоимость, 2 - вода, 3 - доход
        self.time = 0
        self.index = 0
        self.interaction_flag = False

    def update_animation(self, delta_time, animation_time):
        self.time += delta_time
        if self.time >= animation_time / 4 and self.index < 3:
            self.time = 0
            self.index += 1
            self.texture = arcade.load_texture(
                ['images/beet0.png', 'images/beet1.png', 'images/beet2.png', 'images/beet3.png'][self.index])
        if self.index == 3:
            self.interaction_flag = True


class Backet(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/backet.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)


class PacketPotato(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/packet_potato.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)
        self.water = 1


class PacketCarrot(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/packet_carrot.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)
        self.water = 1


class PacketBeet(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/packet_beet.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)
        self.water = 2


class Krest(arcade.Sprite):
    def __init__(self, center_x, center_y, scale=0.4, **kwargs):
        super().__init__(path_or_texture='images/krest.png', center_x=center_x, center_y=center_y, scale=scale,
                         **kwargs)
