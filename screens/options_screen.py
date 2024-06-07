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
        self.components = pygame.sprite.Group(self.volumeController)

    def draw(self, screen: Surface) -> None:
        self.components.draw(screen)
        super().draw(screen)

    def update(self, events: list, keys) -> None:
        self.components.update(events)
        super().update(events, keys)

    def makeCurrent(self) -> None:
        pass
