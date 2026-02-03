import arcade


class SoundPlayer:
    def __init__(self):
        self.title_song = arcade.load_sound('sounds/cool_song.mp3')
        self.coin_pick_up_sound = arcade.load_sound('sounds/coin_pick_up.wav')

    def bg_music_player(self):
        return self.title_song.play(loop=True, volume=0.5)

    def coin_music(self):
        return self.coin_pick_up_sound.play(volume=1)

    def upgrade_music(self):
        return arcade.load_sound('sounds/coin_pick_up.wav').play(volume=1)