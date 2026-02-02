import json

from GUI import *
from items import *
from base import Difficulty

import arcade
from pyglet.graphics import Batch


class Game(arcade.View):
    def __init__(self, default_difficulty: Difficulty):
        super().__init__()

        self.difficulty = default_difficulty

    def to_json(self):
        data = {'score': self.score,
                'total_time': self.total_time,
                'money_k': self.money_k,
                'speed': self.speed,
                'hotbar': [],
                'field': []}

        for i in self.hotbar:
            match type(i):
            if type(i) is Backet:
                data['hotbar'].append('backet')
            elif type(i) is Potato:
                data['hotbar'].append('potato')
            elif type(i) is Carrot:
                data['hotbar'].append('carrot')
            elif type(i) is Beet:
                data['hotbar'].append('beet')
            else:
                data['hotbar'].append('none')

        for i in self.field:
            if type(i) is Backet:
                data['field'].append('backet')
            elif type(i) is Potato:
                data['field'].append('potato')
            elif type(i) is Carrot:
                data['field'].append('carrot')
            elif type(i) is Beet:
                data['field'].append('beet')
            else:
                data['field'].append('none')

        with open('save.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def from_json(self):
        with open('save.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.score = data['score']
        self.total_time = data['total_time']
        self.money_k = data['money_k']
        self.speed = data['speed']

        for i, item in enumerate(data['hotbar']):
            match item:
                case 'backet':
                    self.hotbar[i].item = Backet(self.hotbar[i].center_x, self.hotbar[i].center_y)
                case 'potato':
                    self.hotbar[i].item = PacketPotato(self.hotbar[i].center_x, self.hotbar[i].center_y)
                case 'carrot':
                    self.hotbar[i].item = PacketCarrot(self.hotbar[i].center_x, self.hotbar[i].center_y)
                case 'beet':
                    self.hotbar[i].item = PacketBeet(self.hotbar[i].center_x, self.hotbar[i].center_y)

        for i, item in enumerate(data['field']):
            match item:
                case 'backet':
                    self.hotbar[i].item = Backet(self.hotbar[i].center_x, self.hotbar[i].center_y)
                case 'potato':
                    self.hotbar[i].item = PacketPotato(self.hotbar[i].center_x, self.hotbar[i].center_y)
                case 'carrot':
                    self.hotbar[i].item = PacketCarrot(self.hotbar[i].center_x, self.hotbar[i].center_y)
                case 'beet':
                    self.hotbar[i].item = PacketBeet(self.hotbar[i].center_x, self.hotbar[i].center_y)

    def interaction(self, delta_time):
        self.interaction_flag = True
        arcade.unschedule(self.interaction)
        arcade.schedule(self.update_time, 1)

    def update_time(self, delta_time):
        self.total_time += 1

    def setup(self):
        arcade.unschedule(self.update_time)
        match self.difficulty:
            case Difficulty.EASY:
                self.speed = 1
                self.krest_speed = 3
                self.need_money = 15
            case Difficulty.ADVANCED:
                self.speed = 2
                self.krest_speed = 1
                self.need_money = 50
            case Difficulty.HARD:
                self.speed = 3
                self.krest_speed = 0.5
                self.need_money = 100
            case Difficulty.FREE_GAME:
                self.speed = 1.5
                self.krest_speed = 2

        self.end_view.difficulty = self.difficulty

        self.interaction_flag = False
        arcade.schedule(self.interaction, 1)

        self.money_k = 1
        self.total_time = 0
        self.score = 0
        self.pause_flag = False
        self.background_color = arcade.color.TEA_GREEN
        self.batch = Batch()
        self.coin_batch = Batch()

        self.hotbar = HotBar()
        self.field = Field()
        self.pause_button = Button('images/button_gray.png', center_x=89, center_y=743, scale=0.5)
        self.pause_text = arcade.Text('Пауза', 89, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                      font_size=12, font_name='Press Start 2P')
        self.shop_button = Button('images/button_gray.png', center_x=473, center_y=743, scale=0.5)
        self.shop_text = arcade.Text('Магазин', 473, 743, batch=self.batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.coin_sign = arcade.Sprite('images/coin.png', center_x=344, center_y=743, scale=1.5)
        self.coin_text = arcade.Text('0', 281, 743, batch=self.coin_batch, anchor_x='center', anchor_y='center',
                                     font_size=20, font_name='Press Start 2P')

        if self.need_money:
            self.time_text = arcade.Text('Время: 0 с', 281, 660, batch=self.batch, anchor_x='center', anchor_y='center',
                                         font_size=20, font_name='Press Start 2P')

        self.pause_batch = Batch()
        self.exit_button = Button('images/button_gray.png', center_x=281, center_y=500, scale=0.7)
        self.exit_text = arcade.Text('Выйти', 281, 500, batch=self.pause_batch, anchor_x='center', anchor_y='center',
                                     font_size=12, font_name='Press Start 2P')
        self.return_button = Button('images/button_gray.png', center_x=281, center_y=400, scale=0.7)
        self.return_text = arcade.Text('Вернуться', 281, 400, batch=self.pause_batch, anchor_x='center',
                                       anchor_y='center',
                                       font_size=12, font_name='Press Start 2P')
        self.again_button = Button('images/button_gray.png', center_x=281, center_y=300, scale=0.7)
        self.again_text = arcade.Text('Заново', 281, 300, batch=self.pause_batch, anchor_x='center', anchor_y='center',
                                      font_size=12, font_name='Press Start 2P')

    def on_draw(self):
        self.clear()

        self.hotbar.draw()
        self.field.draw()
        arcade.draw_sprite(self.pause_button)
        arcade.draw_sprite(self.shop_button)
        arcade.draw_sprite(self.coin_sign)
        self.batch.draw()
        self.coin_batch.draw()

        if self.pause_flag:
            arcade.draw_sprite(self.exit_button)
            arcade.draw_sprite(self.return_button)
            arcade.draw_sprite(self.again_button)
            self.pause_batch.draw()

    def on_key_press(self, symbol, modifiers):
        if self.interaction_flag:
            if self.pause_flag and symbol == arcade.key.ESCAPE:
                self.pause_flag = False
            elif not self.pause_flag:
                match symbol:
                    case arcade.key.ESCAPE:
                        self.pause_flag = True
                    case arcade.key.KEY_1:
                        self.hotbar.select(0)
                    case arcade.key.KEY_2:
                        self.hotbar.select(1)
                    case arcade.key.KEY_3:
                        self.hotbar.select(2)
                    case arcade.key.KEY_4:
                        self.hotbar.select(3)

    def on_mouse_release(self, x, y, dx, dy):
        if self.interaction_flag:
            if self.exit_button.left <= x <= self.exit_button.right and \
                    self.exit_button.bottom <= y <= self.exit_button.top and self.pause_flag:
                self.end_view.score = self.total_time
                self.window.show_view(self.end_view)
            if self.return_button.left <= x <= self.return_button.right and \
                    self.return_button.bottom <= y <= self.return_button.top and self.pause_flag:
                self.pause_flag = False
                arcade.schedule(self.update_time, 1)
            if self.again_button.left <= x <= self.again_button.right and \
                    self.again_button.bottom <= y <= self.again_button.top and self.pause_flag:
                self.interaction_flag = False
                self.setup()

            if not self.pause_flag and self.interaction_flag:
                if self.pause_button.left <= x <= self.pause_button.right and \
                        self.pause_button.bottom <= y <= self.pause_button.top:
                    self.pause_flag = True
                    arcade.unschedule(self.update_time)
                if self.shop_button.left <= x <= self.shop_button.right and \
                        self.shop_button.bottom <= y <= self.shop_button.top:
                    self.window.show_view(self.shop_view)

                for i in self.field:
                    if i.interaction_flag and i.cell.left <= x <= i.cell.right and i.cell.bottom <= y <= i.cell.top:
                        if type(i.item) in (PacketPotato, PacketCarrot, PacketBeet) and type(
                                self.hotbar[self.hotbar.selected_cell_id].item) is Backet:
                            self.hotbar[self.hotbar.selected_cell_id].item = None
                            i.item.water -= 1
                            if i.item.water == 0:
                                if type(i.item) == PacketPotato:
                                    i.item = Potato(i.cell.center_x, i.cell.center_y)
                                elif type(i.item) == PacketCarrot:
                                    i.item = Carrot(i.cell.center_x, i.cell.center_y)
                                elif type(i.item) == PacketBeet:
                                    i.item = Beet(i.cell.center_x, i.cell.center_y)
                            break
                        elif type(i.item) in (Potato, Carrot, Beet):
                            self.score += i.item.money * self.money_k
                            i.item = None
                            break
                        elif not i.item and type(self.hotbar[self.hotbar.selected_cell_id].item) in (PacketPotato,
                                                                                                     PacketCarrot,
                                                                                                     PacketBeet):
                            i.item = self.hotbar[self.hotbar.selected_cell_id].item
                            i.item.center_x, i.item.center_y = i.cell.center_x, i.cell.center_y
                            self.hotbar[self.hotbar.selected_cell_id].item = None

    def on_update(self, delta_time):
        self.coin_text.text = str(round(self.score))
        self.time_text.text = f'Время: {self.total_time} с'

        for i in self.field:
            if type(i.item) in (Potato, Carrot, Beet):
                i.item.update_animation(delta_time, self.speed)
                if i.item.index == 3:
                    arcade.schedule(i.disinteraction, self.krest_speed)

        if self.score >= self.need_money:
            self.window.show_view(self.end_view)


class Shop(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.background_color = arcade.color.TEA_GREEN
        self.batch = Batch()

        self.backet_cell = Cell('images/cell.png', 89, 622, item=Backet(89, 622))
        self.backet_text = arcade.Text('Ведро с водой, нужно для полива растений (1 монета)', 89, 490, batch=self.batch,
                                       anchor_x='center', anchor_y='center', font_size=12, font_name='Press Start 2P',
                                       width=128, multiline=True)

        self.money_cell = Cell('images/cell.png', 281, 622, item=arcade.Sprite('images/money_up.png', 0.4, 281, 622))
        self.money_text = arcade.Text('Улучшение: +10% к прибыли (5 монет)', 281, 510, batch=self.batch,
                                      anchor_x='center', anchor_y='center', font_size=12, font_name='Press Start 2P',
                                      width=128, multiline=True)

        self.speed_cell = Cell('images/cell.png', 473, 622, item=arcade.Sprite('images/speed_up.png', 0.4, 473, 622))
        self.speed_text = arcade.Text('Улучшение: на 10% быстрее рост овощей (5 монет)', 473, 500, batch=self.batch,
                                      anchor_x='center',
                                      anchor_y='center', font_size=12, font_name='Press Start 2P', width=128,
                                      multiline=True)

        self.packet_potato_cell = Cell('images/cell.png', 89, 267, item=PacketPotato(89, 267))
        self.packet_potato_text = arcade.Text('Семена картофеля (1 монета)', 89, 155, batch=self.batch,
                                              anchor_x='center', anchor_y='center', font_size=12,
                                              font_name='Press Start 2P', width=128, multiline=True)

        self.packet_carrot_cell = Cell('images/cell.png', 281, 267, item=PacketCarrot(281, 267))
        self.packet_carrot_text = arcade.Text('Семена моркови (2 монеты)', 281, 155, batch=self.batch,
                                              anchor_x='center', anchor_y='center', font_size=12,
                                              font_name='Press Start 2P', width=128, multiline=True)

        self.packet_beet_cell = Cell('images/cell.png', 473, 267, item=PacketBeet(473, 267))
        self.packet_beet_text = arcade.Text('Семена свеклы (3 монеты)', 473, 155, batch=self.batch, anchor_x='center',
                                            anchor_y='center', font_size=12, font_name='Press Start 2P', width=128,
                                            multiline=True)

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

        arcade.draw_sprite(self.game_view.coin_sign)
        self.game_view.coin_batch.draw()

        arcade.draw_sprite(self.exit_button)
        self.batch.draw()

    def on_mouse_release(self, x, y, dx, dy):
        if self.exit_button.left <= x <= self.exit_button.right and \
                self.exit_button.bottom <= y <= self.exit_button.top:
            self.window.show_view(self.game_view)

        if self.money_cell.cell.left <= x <= self.money_cell.cell.right and \
                self.money_cell.cell.bottom <= y <= self.money_cell.cell.top and self.game_view.score >= 5:
            self.game_view.score -= 5
            self.game_view.money_k *= 1.1
        elif self.speed_cell.cell.left <= x <= self.speed_cell.cell.right and \
                self.speed_cell.cell.bottom <= y <= self.speed_cell.cell.top and self.game_view.score >= 5:
            self.game_view.score -= 5
            self.game_view.speed *= 0.9

        for i in self.game_view.hotbar[:-1]:
            if not i.item:
                if self.backet_cell.cell.left <= x <= self.backet_cell.cell.right and \
                        self.backet_cell.cell.bottom <= y <= self.backet_cell.cell.top and self.game_view.score >= 1:
                    self.game_view.score -= 1
                    i.item = Backet(i.cell.center_x, i.cell.center_y)
                    break
                elif self.packet_potato_cell.cell.left <= x <= self.packet_potato_cell.cell.right and \
                        self.packet_potato_cell.cell.bottom <= y <= self.packet_potato_cell.cell.top and \
                        self.game_view.score >= 1:
                    self.game_view.score -= 1
                    i.item = PacketPotato(i.cell.center_x, i.cell.center_y)
                    break
                elif self.packet_carrot_cell.cell.left <= x <= self.packet_carrot_cell.cell.right and \
                        self.packet_carrot_cell.cell.bottom <= y <= self.packet_carrot_cell.cell.top and \
                        self.game_view.score >= 2:
                    self.game_view.score -= 2
                    i.item = PacketCarrot(i.cell.center_x, i.cell.center_y)
                    break
                elif self.packet_beet_cell.cell.left <= x <= self.packet_beet_cell.cell.right and \
                        self.packet_beet_cell.cell.bottom <= y <= self.packet_beet_cell.cell.top and \
                        self.game_view.score >= 3:
                    self.game_view.score -= 3
                    i.item = PacketBeet(i.cell.center_x, i.cell.center_y)
                    break

    def on_update(self, delta_time):
        self.game_view.coin_text.text = str(round(self.game_view.score))
