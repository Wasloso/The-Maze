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
        print(self.rect)
        self.rect.center = start_position
        self.velocity = velocity

    # TODO dodac cos w stylu UP = (0,1), DOWN=(0,-1) itp
    def move(self, x: int, y: int):
        self.rect.x += x * self.velocity
        self.rect.y += y * self.velocity
        return self.rect

    def try_move(self, x: int, y: int):
        new_rect = self.rect.copy()
        new_rect.x += x * self.velocity
        new_rect.y += y * self.velocity
        return new_rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)
