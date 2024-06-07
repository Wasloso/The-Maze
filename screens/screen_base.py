import pygame
from abc import ABC, abstractmethod
from .button import Button

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
        previous=MAIN_MENU,
        backgroundImage: pygame.Surface = None,
    ) -> None:
        """
        Screen class which is base for all screens in the app.
        :param title: Title of the screen
        :param width: Width of the screen
        :param height: Height of the screen
        :param previous: Name of the previous screen
        :param backgroundImage: Background image of the screen, if None, screen will be black
        """
        self.height: int = height
        self.width: int = width
        self.title: str = title
        self.done: bool = False
        self.next_screen: str = None
        self.previous = previous
        if backgroundImage:
            self.backgroundImage = pygame.transform.scale(
                backgroundImage, (self.width, self.height)
            )
        else:
            self.backgroundImage = pygame.Surface((self.width, self.height))
            self.backgroundImage.fill((0, 0, 0))

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.backgroundImage, (0, 0))

    @abstractmethod
    def update(self, events: list, keys) -> None:
        pass

    @abstractmethod
    def makeCurrent(self) -> None:
        # to moze mozna lepiej zrobic, w ogole cale zmienianie ekranow jest mozliwe do poprawienia xd
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.done = False
        self.next_screen = None

    def change_screen(self, next_screen) -> None:
        self.done = True
        self.next_screen = next_screen
