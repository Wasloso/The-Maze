import pygame
from pygame import Surface

from assets.assets_loader import AssetsLoader
from ui_components import UIComponent
from ui_components.button import Button
from ui_components.button_group import ButtonGroup
from ui_components.ui_component import Anchor
from .screen_manager import ScreenManager
from .screen_base import ScreenBase, MAIN_MENU


class MainMenu(ScreenBase):
    def __init__(self, manager, screen_surface: Surface) -> None:
        super().__init__(None, manager, MAIN_MENU)

        self.manager: ScreenManager = manager
        self.screen_surface: Surface = screen_surface
        self.width, self.height = self.screen_surface.get_size()

        self.the_maze_text = UIComponent(
            image=AssetsLoader.get_text("the_maze"),
            anchor=Anchor.MID_TOP
        )

        self.play_button = Button(
            image=AssetsLoader.get_button("play_button"),
            alt_image=AssetsLoader.get_button("play_button", hovered=True),
            desired_size=(300, 100),
            position=(self.width // 2, self.height // 2 - 50),
            callback=lambda: self.manager.maze_selection(self, self.manager),
            anchor = Anchor.CENTER
        )
        self.settings_button = Button(
            image=AssetsLoader.get_button("settings_button"),
            alt_image=AssetsLoader.get_button("settings_button", hovered=True),
            desired_size=(550, 100),
            position=(self.width // 2, self.height // 2 + 100),
            callback=lambda: self.manager.settings(self, self.manager),
            anchor=Anchor.CENTER
        )
        self.quit_button = Button(
            image=AssetsLoader.get_button("quit_button"),
            alt_image=AssetsLoader.get_button("quit_button", hovered=True),
            desired_size=(150, 50),
            position=(100, self.height - 75),
            callback=lambda: self.manager.back(None),
            anchor=Anchor.BOTTOM_LEFT
        )
        self.credits_button = Button(
            image=AssetsLoader.get_button("credits_button"),
            alt_image=AssetsLoader.get_button("credits_button", hovered=True),
            desired_size=(225, 50),
            position=(self.width - 100, self.height - 75),
            callback=lambda: self.manager.credits(self, self.manager),
            anchor=Anchor.BOTTOM_RIGHT
        )

        self.buttons = ButtonGroup(
            self.play_button,
            self.settings_button,
            self.quit_button,
            self.credits_button,
        )

    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        self.the_maze_text.draw(surface, (surface.get_width() // 2, 50))
        self.buttons.draw(surface)

    def update(self, events, keys) -> None:
        for event in events:
            self.buttons.update(event)
