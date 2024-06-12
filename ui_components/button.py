import pygame
from pygame.sprite import Sprite
from pygame.font import Font
from .ui_component import UIComponent
import sys

sys.path.append("../")
from assets.assets_loader import AssetsLoader


class Button(UIComponent):
    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        image: pygame.Surface = None,
        altImage: pygame.Surface = None,
        callback: callable = None,
        desiredSize=(200, 100),
    ) -> None:
        """Image is the main display image. Altimage appears when the button is hovered"""
        super().__init__(position, desiredSize, image)
        self.altImage = (
            pygame.transform.scale(altImage, desiredSize) if altImage else None
        )
        self.rect.center = position
        self.displayImage = self.image
        self.callback = callback

    def draw(self, screen: pygame.Surface, position: tuple[int, int] = None) -> None:
        if not position:
            position = self.rect
        elif position != self.rect:
            self.rect.topleft = position
        screen.blit(self.displayImage, position)

    def update(self, event: pygame.event.Event) -> None:
        hovered = self.check_hovered()
        self.displayImage = (
            self.image if not hovered or not self.altImage else self.altImage
        )
        if event.type == pygame.MOUSEBUTTONDOWN and hovered and self.callback:
            self.callback()

    @staticmethod
    def go_back_button(
        position: tuple[int, int],
        callback: callable,
        desiredSize=(100, 100),
    ) -> Sprite:
        return Button(
            position,
            AssetsLoader.get_button("back_button"),
            AssetsLoader.get_button("back_button", hovered=True),
            callback,
            desiredSize,
        )
