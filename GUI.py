import arcade

from items import Backet


class Cell(arcade.Sprite):
    def __init__(self, path_or_texture, center_x, center_y, item=None, scale=1, **kwargs):
        super().__init__(**kwargs)
        self.is_selected = False
        self.item = item
        self.cell = arcade.Sprite(path_or_texture, center_x=center_x, center_y=center_y, scale=scale)

    def add_item(self, item):
        self.item = item

    def draw(self):
        arcade.draw_sprite(self.cell)
        if self.item:
            arcade.draw_sprite(self.item)


class HotBar(arcade.SpriteList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(4):
            self.append(Cell('images/cell.png', 97 + 128 * i, 97, Backet(97 + 128 * i, 97)))
        self.selected_cell_id = 0
        self.append(Cell('images/selected_cell.png', 97 + 128 * self.selected_cell_id, 97, scale=0.5))
        self.select(0)

    def select(self, cell_id):
        self[self.selected_cell_id].is_selected = False
        self.selected_cell_id = cell_id
        self[self.selected_cell_id].is_selected = True
        self[-1].cell.center_x = 97 + 128 * self.selected_cell_id

    def draw(self):
        for cell in self:
            cell.draw()


class Field(arcade.SpriteList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(3):
            for j in range(3):
                self.append(Cell('images/field_cell.png', 153 + 128 * j, 97 + 128 * (i + 1.7)))

    def draw(self):
        for cell in self:
            arcade.draw_sprite(cell.cell)
            if cell.item:
                arcade.draw_sprite(cell.item)


class Button(arcade.Sprite):
    def __init__(self, path_or_texture, center_x, center_y, scale=1, **kwargs):
        super().__init__(path_or_texture=path_or_texture, center_x=center_x, center_y=center_y, scale=scale, **kwargs)