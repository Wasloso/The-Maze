from abc import ABC, abstractmethod

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
    def __init__(
            self,
            width: int,
            height: int,
            manager,
            screenName: str = MAIN_MENU,
            previous=MAIN_MENU,
    ) -> None:
        """
        Screen class which is base for all screens in the app.
        :param width: Width of the screen
        :param height: Height of the screen
        :param previous: Name of the previous screen
        :param backgroundImage: Background image of the screen, if None, screen will be black
        """
        self.screenName = screenName
        self.height: int = height
        self.width: int = width
        self.manager = manager

        self.done: bool = False
        self.next_screen: str = None
        self.previous = previous
        self.background = UIComponent(
            (0, 0),
            (width, height),
            AssetsLoader.get_background(screenName),
        )

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        UIComponent((0, 0), screen.get_size(), )
        self.background.draw(screen)

    @abstractmethod
    def update(self, events: list, keys) -> None:
        pass
