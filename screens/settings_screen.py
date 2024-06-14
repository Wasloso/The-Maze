from ui_components.button import Button
from .screen_base import *
import pygame
from pygame.surface import Surface
import sys

sys.path.append("../")
from ui_components.volume_controller import VolumeController
from ui_components.ui_component import UIComponent
from data import SettingsManager


class SettingsScreen(ScreenBase):
    def __init__(
        self,
        previous_screen: Optional[ScreenBase],
        manager,
        settings_manager: SettingsManager,
    ) -> None:
        super().__init__(previous_screen, manager, screen_name=SETTINGS)
        self.settings_manager: SettingsManager = settings_manager
        self.volume_controller = VolumeController(
            (100, 0), (500, 100), settings_manager
        )
        self.title = UIComponent(
            image=AssetsLoader.get_button("settings_button"),
            desired_size=(550, 100),
        )

        self.back_button = Button.go_back_button(
            position=(50, 50), callback=lambda: manager.back(previous_screen)
        )

    def draw(self, surface: Surface) -> None:
        super().draw(surface)
        self.title.draw(
            surface,
            position=(surface.get_rect().width // 2 - self.title.rect.width // 2, 50),
        )
        self.back_button.draw(surface)
        self.volume_controller.draw(
            surface,
            position=(
                surface.get_rect().width // 2 - self.volume_controller.rect.width // 2,
                surface.get_rect().height // 2
                - self.volume_controller.rect.height // 2,
            ),
        )

    def update(self, events: list, keys) -> None:
        for event in events:
            self.back_button.update(event)
            self.volume_controller.update(event)
        super().update(events, keys)
