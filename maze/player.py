import pygame


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        start_position: tuple[int, int],
        velocity: float,
        size: int = 15,
        image: pygame.Surface = None,
    ):
        super().__init__()
        if image is None:
            self.image = pygame.Surface((size, size))
            self.image.fill((255, 255, 255))
        else:
            # TODO jak to zrobic zeby ladnie dopasowywalo kolizje do obrazka kiedy ma przezroczystosc
            image = image.convert()
            self.image: pygame.Surface = pygame.Surface((30, 30), pygame.SRCALPHA)
            pygame.transform.scale(
                image, self.image.get_size(), dest_surface=self.image
            )
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

    def draw(self, screen):
        screen.blit(self.image, self.rect)
