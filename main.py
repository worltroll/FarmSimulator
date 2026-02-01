import arcade

from db_manager import DBManager
from base import Window, StartView, EndView, Difficulty, Titles
from game_base import Game, Shop


def main():
    window = Window(562, 800, 'Симулятор фермы')
    db = DBManager()

    arcade.load_font('fonts/PressStart2P-Regular.ttf')

    game = Game(Difficulty.EASY)

    shop = Shop()
    shop.game_view = game
    shop.setup()

    start_view = StartView(game)
    start_view.setup()

    titles = Titles(start_view)
    titles.setup()
    start_view.titles = titles

    end_view = EndView(db, start_view)
    end_view.setup()
    start_view.end_view = end_view

    game.start_view = start_view
    game.shop_view = shop
    game.end_view = end_view

    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
