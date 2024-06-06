from pygame.sprite import Sprite
from pygame import Surface


class Objective(Sprite):
    def __init__(self, position: tuple[int, int], size: int = 15):
        super().__init__()
        self.image = Surface((size, size))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

    def check_collision(self, rect):
        return self.rect.colliderect(rect)
