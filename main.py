import arcade

from db_manager import DBManager
from base import Window, StartView
from game_base import Game


def main():
    window = Window(562, 800, 'Симулятор фермы')
    db = DBManager()

    arcade.load_font('fonts/PressStart2P-Regular.ttf')

    game = Game()
    game.setup()

    start_view = StartView(game)
    start_view.setup()

    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
