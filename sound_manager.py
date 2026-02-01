import arcade


class SoundPlayer:
    def __init__(self):
        self.title_song = arcade.load_sound('sounds/cool_song.mp3')

    def bg_music_player(self):
        return self.title_song.play(loop=True, volume=0.5)
