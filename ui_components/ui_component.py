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
        position: tuple[int, int] = (0, 0),
        desiredSize: tuple[int, int] = None,
        image: Surface = None,
        fill: tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        super().__init__()
        if not image:
            self.image = Surface(10, 10)
            self.image.fill(fill)
        elif desiredSize:
            self.image = scale(image, desiredSize)
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, screen: Surface, position: tuple[int, int] = None) -> None:
        if not position:
            position = self.rect
        else:
            self.rect.topleft = position
        screen.blit(self.image, position)

    def update(self, event: Event) -> None:
        pass

    def check_hovered(self):
        pos = mouse.get_pos()
        return self.rect.collidepoint(pos)
