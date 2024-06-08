import pygame
from abc import ABC, abstractmethod
import sys

sys.path.append("../")
from assets.assets_loader import AssetsLoader
from ui_components.ui_component import UIComponent


# TODO maybe it can be moved somewhere else eg. constants.py so it can be used everywhere (assets manager)
MAIN_MENU = "main_menu_screen"
PLAY = "play_screen"
OPTIONS = "options_screen"
GAME = "game_screen"
CREDITS = "credits_screen"


class ScreenBase(ABC):
    # TODO the title is useless i guess
    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        screenName: str = MAIN_MENU,
        previous=MAIN_MENU,
    ) -> None:
        """
        Screen class which is base for all screens in the app.
        :param title: Title of the screen
        :param width: Width of the screen
        :param height: Height of the screen
        :param previous: Name of the previous screen
        :param backgroundImage: Background image of the screen, if None, screen will be black
        """
        self.screenName = screenName
        self.height: int = height
        self.width: int = width
        self.title: str = title
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
        self.background.draw(screen)

    @abstractmethod
    def update(self, events: list, keys) -> None:
        pass

    def makeCurrent(self) -> None:
        # to moze mozna lepiej zrobic, w ogole cale zmienianie ekranow jest mozliwe do poprawienia xd
        self.done = False
        self.next_screen = None

    def change_screen(self, next_screen) -> None:
        self.done = True
        self.next_screen = next_screen
