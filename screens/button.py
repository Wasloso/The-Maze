import pygame
from pygame.sprite import Sprite
from pygame.font import Font


class Button(Sprite):
    def __init__(
        self,
        position: tuple[int, int],
        image: pygame.Surface,
        callback: callable = None,
    ) -> None:
        super().__init__()
        self.image = image
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
                    print(f"Button clicked!")
