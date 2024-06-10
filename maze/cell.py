from pygame.sprite import Sprite
from pygame import *
from pygame.rect import Rect


class Cell:
    def __init__(self, size: int, x: int, y: int, collidable: bool = False) -> None:
        self.rect = Rect(x, y, size, size)
        self.collidable = collidable
        self.size = size

    def change_collidable(self, collidable=False) -> None:
        if collidable:
            self.collidable = collidable
        else:
            self.collidable = not self.collidable
