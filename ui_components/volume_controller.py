import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from .button import Button
from .ui_component import UIComponent


class VolumeController(UIComponent):
    def __init__(self, position, desired_size) -> None:
        image = Surface(desired_size, pygame.SRCALPHA)
        super().__init__(position, desired_size, image.convert_alpha())

    def draw(self, screen: Surface) -> None:
        super().draw(screen)
