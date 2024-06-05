import pygame
from abc import ABC, abstractmethod

MAIN_MENU = "main_menu_screen"
PLAY = "play_screen"
OPTIONS = "options_screen"
GAME = "game_screen"


class ScreenBase(ABC):
    def __init__(self, title: str, width: int, height: int) -> None:
        self.height: int = height
        self.width: int = width
        self.title: str = title
        self.done: bool = False
        self.next_screen: str = None

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 0))

    @abstractmethod
    def update(self, events: list, keys) -> None:
        pass

    @abstractmethod
    def makeCurrent(self) -> None:
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.done = False
        self.next_screen = None

    def change_screen(self, next_screen) -> None:
        self.done = True
        self.next_screen = next_screen
