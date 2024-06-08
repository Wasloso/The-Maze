from .screen_base import *
import pygame
from pygame.sprite import Group
import sys

sys.path.append("../")
from ui_components.button import Button
from ui_components.volume_controller import VolumeController
from assets.assets_loader import AssetsLoader


class CreditsScreen(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height, screenName=CREDITS)
        self.back_button = Button.go_back_button(
            (0, 0), lambda: self.change_screen(MAIN_MENU)
        )

    def draw(self, screen: pygame.Surface) -> None:
        super().draw(screen)
        self.back_button.draw(screen)

    def update(self, events, keys) -> None:
        for event in events:
            self.back_button.update(event)
        super().update(events, keys)
