from pygame.sprite import Sprite
from pygame import *


class Cell:
    def __init__(self, size: int, x: int, y: int, collidable: bool = False) -> None:
        self.image = Surface((size, size))
        self.image.fill((255, 0, 0) if collidable else (0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collidable = collidable
        self.size = size

    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, self.rect)

    def change_collidable(self, collidable=False) -> None:
        if collidable:
            self.collidable = collidable
        else:
            self.collidable = not self.collidable
        self.image.fill((255, 0, 0) if self.collidable else (0, 255, 0))

    def __repr__(self) -> str:
        return f"Cell({self.size}, {self.rect.x}, {self.rect.y}, {self.collidable})"
