from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

import pygame

from assets.assets_loader import AssetsLoader
from ui_components.ui_component import UIComponent

# TODO maybe it can be moved somewhere else eg. constants.py so it can be used everywhere (assets manager)
MAIN_MENU = "main_menu_screen"
PLAY = "play_screen"
OPTIONS = "options_screen"
GAME = "game_screen"
CREDITS = "credits_screen"


class ScreenBase(ABC):
    def __init__(self, previous_screen: Optional[ScreenBase], manager, screen_name: str = MAIN_MENU) -> None:
        self.previous_screen = previous_screen
        self.screen_name = screen_name
        self.manager = manager

    def draw(self, surface: pygame.Surface) -> None:
        UIComponent((0, 0), surface.get_size(), AssetsLoader.get_background(self.screen_name)).draw(surface)

    @abstractmethod
    def update(self, events: list, keys) -> None:
        pass
