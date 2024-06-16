import json
import pygame


class SettingsManager:
    def __init__(self, path="data/settings.json"):
        self.path = path
        self.settings = None
        self.volume = None
        self.mute: bool = False

    def load_settings(self):
        try:
            with open(self.path, "r") as f:
                self.settings = json.load(f)
                self.volume = self.settings["sound"]["volume"]
                self.mute = self.settings["sound"]["mute"]
        except FileNotFoundError:
            self.volume = 100
            self.mute = False
            self.settings = {
                "sound": {
                    "volume": self.volume,
                    "mute": self.mute,
                }
            }
            self.save_settings()
        self.set_game_volume()

    def save_settings(self):
        with open(self.path, "w") as f:
            data = json.dumps(self.settings, indent=4)
            f.write(data)

    def change_volume(self, increase: bool) -> int:
        if increase and self.volume != 100:
            self.volume += 10
        elif not increase and self.volume != 0:
            self.volume -= 10
        self.settings["sound"]["volume"] = self.volume
        self.set_game_volume()
        return self.volume

    def toggle_mute(self) -> bool:
        self.mute = not self.mute
        self.settings["sound"]["mute"] = self.mute
        self.set_game_volume()
        return self.mute

    def set_game_volume(self) -> None:
        pygame.mixer.music.set_volume(0 if self.mute else self.volume / 100)
