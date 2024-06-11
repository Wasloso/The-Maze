from ui_components.button import Button
from .screen_base import *
import pygame
from pygame.surface import Surface
import sys

sys.path.append("../")
from ui_components.volume_controller import VolumeController
from ui_components.ui_component import UIComponent


class SettingsScreen(ScreenBase):
    def __init__(self, previous_screen: Optional[ScreenBase], manager) -> None:
        super().__init__(previous_screen, manager, screen_name=SETTINGS)
        self.volumeController = VolumeController((100, 0), (100, 100))
        self.title = UIComponent(
            image=AssetsLoader.get_button("settings_button"),
            desiredSize=(550, 100),
            position=(400, 50),
        )

        self.back_button = Button.go_back_button(
            position=(50, 50), callback=lambda: manager.back(previous_screen)
        )
        self.components = pygame.sprite.Group(self.volumeController, self.title)

    def draw(self, surface: Surface) -> None:
        super().draw(surface)
        self.back_button.draw(surface)
        self.components.draw(surface)

    def update(self, events: list, keys) -> None:
        for event in events:
            self.components.update(event)
            self.back_button.update(event)
        super().update(events, keys)
