import pygame
from abc import ABC, abstractmethod
import sys

sys.path.append("../")
from ui_components.ui_component import UIComponent

MAIN_MENU = "main_menu_screen"
PLAY = "play_screen"
OPTIONS = "options_screen"
GAME = "game_screen"


class ScreenBase(ABC):
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
            pygame.image.load(f"assets/backgrounds/{self.screenName}.png"),
        )

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        self.background.draw(screen)

    @abstractmethod
    def update(self, events: list, keys) -> None:
        pass

    @abstractmethod
    def makeCurrent(self) -> None:
        # to moze mozna lepiej zrobic, w ogole cale zmienianie ekranow jest mozliwe do poprawienia xd
        self.done = False
        self.next_screen = None

    def change_screen(self, next_screen) -> None:
        self.done = True
        self.next_screen = next_screen
