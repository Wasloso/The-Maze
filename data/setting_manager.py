import json
import pygame
import os
from assets.assets_loader import AssetsLoader


class SettingsManager:
    def __init__(
        self, path: str = f"{os.path.dirname(__file__)}/settings.json"
    ) -> None:
        self.path: str = path
        self.settings: dict[str, bool | int] = None
        self.volume: int = None
        self.mute: bool = False

    def load_settings(self) -> None:
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
        self.load_background_music("background")
        self.set_game_volume()

    def save_settings(self) -> None:
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

    def load_background_music(self, name: str) -> None:
        AssetsLoader.load_music("background")
        pygame.mixer.music.play(-1)

    def set_game_volume(self) -> None:
        pygame.mixer.music.set_volume(0 if self.mute else self.volume / 100)
