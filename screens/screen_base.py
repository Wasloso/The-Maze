import pygame
from abc import ABC, abstractmethod


class ScreenBase(ABC):
    def __init__(self, title: str, width: int, height: int) -> None:
        self.height: int = height
        self.width: int = width
        self.title: str = title

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
