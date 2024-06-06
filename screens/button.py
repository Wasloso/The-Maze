import pygame
from pygame.sprite import Sprite
from pygame.font import Font


class Button(Sprite):
    def __init__(
        self,
        text: str,
        position: tuple[int, int],
        font: Font,
        callback: callable = None,
    ) -> None:
        super().__init__()
        self.text = text
        self.font = font
        self.image = self.font.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.callback = callback

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def update(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                else:
                    print(f"Button {self.text} clicked!")
