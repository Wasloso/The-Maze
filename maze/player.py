from enum import Enum

import pygame
from pygame.surface import Surface


class Direction(Enum):
    UP: tuple[int, int] = (0, -1)
    DOWN: tuple[int, int] = (0, 1)
    LEFT: tuple[int, int] = (-1, 0)
    RIGHT: tuple[int, int] = (1, 0)


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        start_position: tuple[int, int],
        velocity: float,
        image: Surface,
        size: int = 15,
    ):
        super().__init__()
        self.image: Surface = pygame.transform.scale(image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = start_position
        self.velocity: float = velocity

    def move(self, direction: tuple[int, int], multiplier: int = 1) -> None:
        x, y = direction
        self.rect.x += x * self.velocity * multiplier
        self.rect.y += y * self.velocity * multiplier

    def try_move(self, direction: Direction, multiplier: int = 1) -> pygame.Rect:
        x, y = direction.value
        new_rect = self.rect.copy()
        new_rect.x += x * self.velocity * multiplier
        new_rect.y += y * self.velocity * multiplier
        return new_rect

    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, self.rect)

    def update(self, events, keys):
        pass
