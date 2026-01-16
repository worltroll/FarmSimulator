import arcade
from base import Window
from game_base import Game


def main():
    window = Window(562, 800, 'Симулятор фермы')
    game = Game()
    game.setup()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()