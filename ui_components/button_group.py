import pygame.sprite

from .button import Button


class ButtonGroup(pygame.sprite.Group):
    def __init__(self, *sprites: Button):
        super().__init__(*sprites)

    def draw(self, surface, **kwargs):
        for sprite in self.sprites():
            sprite.draw(surface)

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update(*args, **kwargs)
