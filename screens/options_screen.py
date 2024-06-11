from ui_components.button import Button
from .screen_base import *
import pygame
from pygame.surface import Surface
import sys

sys.path.append("../")
from ui_components.volume_controller import VolumeController


class OptionsScreen(ScreenBase):
    def __init__(self, previous_screen: Optional[ScreenBase], manager) -> None:
        super().__init__(previous_screen, manager, screen_name=OPTIONS)
        self.volumeController = VolumeController((100, 0), (100, 100))
        self.back_button = Button.go_back_button(
            (0, 0), lambda: manager.back(previous_screen)
        )
        self.components = pygame.sprite.Group(self.volumeController)

    def draw(self, surface: Surface) -> None:
        super().draw(surface)
        self.back_button.draw(surface)
        self.components.draw(surface)

    def update(self, events: list, keys) -> None:
        for event in events:
            self.components.update(event)
            self.back_button.update(event)
        super().update(events, keys)
