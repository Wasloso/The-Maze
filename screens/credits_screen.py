from .screen_base import *
import pygame
from pygame.sprite import Group
import sys
from pygame.surface import Surface

sys.path.append("../")
from ui_components.button import Button
from ui_components.volume_controller import VolumeController
from assets.assets_loader import AssetsLoader


class CreditsScreen(ScreenBase):
    def __init__(self, previous_screen: Optional[ScreenBase], manager) -> None:
        super().__init__(previous_screen, manager, screen_name=CREDITS)
        self.back_button = Button.go_back_button(
            position=(50, 50), callback=lambda: self.manager.back(previous_screen)
        )
        self.text = pygame.transform.scale(
            AssetsLoader.get_button("selection_button"), (600, 400)
        )
        UIComponent.add_text_to_surface(
            text=["Made by", "Tymoteusz Lango", "&", "Patryk Łuszczek"],
            surface=self.text,
            font=pygame.font.Font(None, 80),
            text_color=(0, 0, 0),
        )

    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        self.back_button.draw(surface)
        surface.blit(
            self.text,
            (
                surface.get_width() // 2 - self.text.get_width() // 2,
                surface.get_height() // 2 - self.text.get_height() // 2,
            ),
        )

    def update(self, events, keys) -> None:
        for event in events:
            self.back_button.update(event)
        super().update(events, keys)
