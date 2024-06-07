from pygame.transform import scale
from pygame.sprite import Sprite
from pygame import Surface
from pygame.event import Event
from pygame import mouse


"""Base class for all UI components"""
""" Can be initialized on its own but without any special functionality"""
"""Can be inherited to create more complex UI components like buttons"""


class UIComponent(Sprite):
    def __init__(
        self,
        position: tuple[int, int],
        image: Surface,
        desiredSize: tuple[int, int],
        fill: tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        super().__init__()
        if not image:
            self.image = Surface(desiredSize)
            self.image.fill(fill)
        else:
            self.image = scale(image, desiredSize)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, self.rect)

    def update(self, event: Event) -> None:
        pass

    def check_hovered(self):
        pos = mouse.get_pos()
        return self.rect.collidepoint(pos)
