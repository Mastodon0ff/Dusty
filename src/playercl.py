import vlc
import time
import pathlib

class Player:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def load(self, path):
        media = self.instance.media_new(path)
        self.player.set_media(media)
    
    def play(self):
        self.player.play()
        time.sleep(1)
        while self.player.is_playing():
            time.sleep(1)

    def play_dir(self, path):
        folder_path = pathlib.Path(path)
        for file in folder_path.rglob("*.mka"): # will add more formats after testing function
            self.load(file)
            self.play()

    def stop(self):
        self.player.stop()

    def set_volume(self, volume):
        self.player.audio_set_volume(volume)

    def seek(self, seconds):
        self.player.set_time(seconds * 1000)