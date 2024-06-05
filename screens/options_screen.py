from .screen_base import ScreenBase
from pygame import *


class OptionsScreen(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height)

    def draw(self, screen: Surface) -> None:
        pass

    def update(self, events: list) -> None:
        pass

    def makeCurrent(self) -> None:
        pass
