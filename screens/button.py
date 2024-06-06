import pygame
from pygame.sprite import Sprite
from pygame.font import Font


class Button(Sprite):
    def __init__(
        self,
        position: tuple[int, int],
        image: pygame.Surface,
        altImage: pygame.Surface = None,
        callback: callable = None,
        desiredSize=(200, 100),
    ) -> None:
        super().__init__()
        self.image = pygame.transform.scale(image, desiredSize)
        self.altImage = (
            pygame.transform.scale(altImage, desiredSize) if altImage else None
        )
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.displayImage = self.image
        self.desiredSize = desiredSize
        self.callback = callback

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.displayImage, self.rect)

    def update(self, event: pygame.event.Event) -> None:
        pos = pygame.mouse.get_pos()
        hovered = self.rect.collidepoint(pos)
        self.displayImage = (
            self.image if not hovered or not self.altImage else self.altImage
        )
        if event.type == pygame.MOUSEBUTTONDOWN and hovered:
            self.callback()
