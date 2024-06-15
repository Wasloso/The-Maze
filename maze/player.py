import pygame
from pygame.surface import Surface


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        start_position: tuple[int, int],
        velocity: float,
        image: Surface = None,
        size: int = 15,
    ):
        super().__init__()
        self.image = pygame.transform.scale(image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = start_position
        self.velocity = velocity
        self.directions = {
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0),
        }

    # TODO dodac cos w stylu UP = (0,1), DOWN=(0,-1) itp
    def move(self, direction, multiplier=1):
        x, y = self.directions[direction]
        self.rect.x += x * self.velocity * multiplier
        self.rect.y += y * self.velocity * multiplier
        return self.rect

    def try_move(self, direction, multiplier=1):
        x, y = self.directions[direction]
        new_rect = self.rect.copy()
        new_rect.x += x * self.velocity * multiplier
        new_rect.y += y * self.velocity * multiplier
        return new_rect

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

    def update(self, events, keys): ...
