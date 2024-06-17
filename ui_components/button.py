from __future__ import annotations

import pygame

from .ui_component import UIComponent
from assets.assets_loader import AssetsLoader


class Button(UIComponent):
    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        image: pygame.Surface = None,
        alt_image: pygame.Surface = None,
        callback: callable = None,
        desired_size=(200, 100),
    ) -> None:
        """Image is the main display image. alt_image appears when the button is hovered"""
        super().__init__(position, desired_size, image)
        self.desired_size = desired_size
        self.altImage = (pygame.transform.scale(alt_image, desired_size) if alt_image else None)
        self.rect.center = position  # FIXME: change to topleft for consitency (need to adjust some positions in other files)
        self.displayImage = self.image
        self.callback = callback

    def draw(self, screen: pygame.Surface, position: tuple[int, int] = None) -> None:
        if not position:
            position = self.rect.topleft
        elif position != self.rect:
            self.rect.topleft = position
        screen.blit(self.displayImage, position)

    def update(self, event: pygame.event.Event) -> None:
        hovered = self.check_hovered()
        self.displayImage = (
            self.image if not hovered or not self.altImage else self.altImage
        )
        if (
            self.callback
            and hovered
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == pygame.BUTTON_LEFT
        ):
            self.callback()

    @staticmethod
    def go_back_button(
        position: tuple[int, int],
        callback: callable,
        desired_size=(100, 100),
    ) -> Button:
        return Button(
            position,
            AssetsLoader.get_button("back_button"),
            AssetsLoader.get_button("back_button", hovered=True),
            callback,
            desired_size,
        )

    def change_image(
        self, image: pygame.Surface = None, alt_image: pygame.Surface = None
    ) -> None:
        if image:
            self.image = pygame.transform.scale(image, self.desired_size)
        if alt_image:
            self.altImage = pygame.transform.scale(alt_image, self.desired_size)
