from enum import Enum

from pygame.transform import scale
from pygame.sprite import Sprite
from pygame import Surface
from pygame import mouse
from pygame.font import Font


class Anchor(Enum):
    TOP_LEFT = 'topleft'
    MID_TOP = 'midtop'
    TOP_RIGHT = 'topright'
    MID_RIGHT = 'midright'
    BOTTOM_RIGHT = 'bottomright'
    MID_BOTTOM = 'midbottom'
    BOTTOM_LEFT = 'bottomleft'
    MID_LEFT = 'midleft'
    CENTER = 'center'


class UIComponent(Sprite):
    """
        Base class for all UI components.
        Can be initialized on its own but without any special functionality.
        Can be inherited to create more complex UI components like buttons
    """

    def __init__(
            self,
            position: tuple[int, int] = None,
            desired_size: tuple[int, int] = None,
            image: Surface = None,
            fill: tuple[int, int, int] = (0, 0, 0),
            anchor: Anchor = Anchor.TOP_LEFT
    ) -> None:
        super().__init__()
        self.desired_size = desired_size
        if not image:
            self.image = Surface(desired_size if desired_size else (10, 10))
            self.image.fill(fill)
        elif desired_size:
            self.image = scale(image, desired_size)
        else:
            self.image = image
        self.rect = self.image.get_rect()

        self.anchor = anchor.value
        self.move(position)

    def move(self, position: tuple[int, int]) -> None:
        if position:
            current_anchor_pos = getattr(self.rect, self.anchor)
            self.rect.move_ip(position[0] - current_anchor_pos[0], position[1] - current_anchor_pos[1])

    def draw(self, screen: Surface, position: tuple[int, int] = None) -> None:
        self.move(position)
        screen.blit(self.image, self.rect)

    def check_hovered(self):
        return self.rect.collidepoint(mouse.get_pos())

    def change_image(self, image: Surface) -> None:
        self.image = scale(image, self.desired_size)

    @staticmethod
    def add_text_to_surface(
            text: str | list[str],
            font: Font,
            text_color: tuple[int, int, int],
            surface: Surface,
    ) -> Surface:
        if type(text) == list:
            for i, line in enumerate(text):
                text_surface = font.render(line, True, text_color)
                text_rect = text_surface.get_rect(
                    center=(
                        surface.get_width() // 2,
                        surface.get_height() // (len(text) + 1)
                        + (i + 1) * font.size(" ")[1],
                    )
                )
                surface.blit(text_surface, text_rect)
                surface.blit(text_surface, text_rect.topleft)
        else:
            text_surface = font.render(text, True, text_color)
            text_rect = text_surface.get_rect(center=(surface.get_rect().center))
            surface.blit(text_surface, text_rect.topleft)
        return surface
