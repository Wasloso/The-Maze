import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from .button import Button
from .ui_component import UIComponent


class VolumeController(UIComponent):
    def __init__(self, position, desiredSize) -> None:
        image = Surface(desiredSize, pygame.SRCALPHA)
        super().__init__(position, image.convert_alpha(), desiredSize)

    def draw(self, screen: Surface) -> None:
        pass
