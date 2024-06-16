from enum import Enum

import pygame
from pygame.surface import Surface


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Player(pygame.sprite.Sprite):
    def __init__(
            self,
            start_position: tuple[int, int],
            velocity: float,
            image: Surface,
            size: int = 15,
    ):
        super().__init__()
        self.image = pygame.transform.scale(image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = start_position
        self.velocity = velocity

    def move(self, direction, multiplier=1):
        x, y = direction
        self.rect.x += x * self.velocity * multiplier
        self.rect.y += y * self.velocity * multiplier

    def try_move(self, direction: Direction, multiplier=1):
        x, y = direction.value
        new_rect = self.rect.copy()
        new_rect.x += x * self.velocity * multiplier
        new_rect.y += y * self.velocity * multiplier
        return new_rect

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

    def update(self, events, keys):
        ...
