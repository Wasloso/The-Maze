from pygame.sprite import Sprite
from pygame import Surface
from pygame.transform import scale
from assets.assets_loader import AssetsLoader


class Objective(Sprite):
    def __init__(self, position: tuple[int, int], size: int = 15):
        super().__init__()
        self.image: Surface = scale(AssetsLoader.get_objective(), (size, size))
        self.reachedImage: Surface = scale(
            AssetsLoader.get_objective(reached=True), (size, size)
        )
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, self.rect)

    def check_collision(self, rect) -> None:
        reached = self.rect.colliderect(rect)
        if reached:
            self.image = self.reachedImage
        return reached
