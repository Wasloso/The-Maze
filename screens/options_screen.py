from ui_components.button import Button
from .screen_base import *
import pygame
from pygame.surface import Surface
import sys

sys.path.append("../")
from ui_components.volume_controller import VolumeController


class OptionsScreen(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height, screenName=OPTIONS)
        self.volumeController = VolumeController((100, 0), (100, 100))
        self.back_button = Button.go_back_button(
            (0, 0), lambda: self.change_screen(MAIN_MENU)
        )
        self.components = pygame.sprite.Group(self.volumeController)

    def draw(self, screen: Surface) -> None:
        super().draw(screen)
        self.back_button.draw(screen)
        self.components.draw(screen)

    def update(self, events: list, keys) -> None:
        for event in events:
            self.components.update(event)
            self.back_button.update(event)
        super().update(events, keys)
