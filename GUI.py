import arcade


class Cell(arcade.Sprite):
    def __init__(self, path_or_texture, center_x, center_y, scale=1, **kwargs):
        super().__init__(path_or_texture=path_or_texture, scale=scale, center_x=center_x, center_y=center_y,
                         **kwargs)
        self.is_selected = False


class HotBar(arcade.SpriteList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(4):
            self.append(Cell('images/cell.png', 97 + 128 * i, 97))
        self.selected_cell_id = 0
        self.append(Cell('images/selected_cell.png', 97 + 128 * self.selected_cell_id, 97))
        self.select(0)

    def select(self, cell_id):
        self[self.selected_cell_id].is_selected = False
        self.selected_cell_id = cell_id
        self[self.selected_cell_id].is_selected = True
        self[-1].center_x = 97 + 128 * self.selected_cell_id


class Field(arcade.SpriteList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(4):
            for j in range(7):
                self.append(Cell('images/cell.png', 97 + 128 * j, 97 + 128 * (i + 2)))