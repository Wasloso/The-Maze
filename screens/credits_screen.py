from .screen_base import *
import pygame
from pygame.sprite import Group
import sys

sys.path.append("../")
from ui_components.button import Button
from ui_components.volume_controller import VolumeController
from assets.assets_loader import AssetsLoader


class CreditsScreen(ScreenBase):
    def __init__(self, previous_screen: Optional[ScreenBase], manager) -> None:
        super().__init__(previous_screen, manager, screen_name=CREDITS)
        self.back_button = Button.go_back_button((0, 0), lambda: self.manager.back(previous_screen))

    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        self.back_button.draw(surface)

    def update(self, events, keys) -> None:
        for event in events:
            self.back_button.update(event)
        super().update(events, keys)
