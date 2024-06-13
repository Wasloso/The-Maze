import json

from pygame import Surface

from ui_components import UIComponent
from . import ScreenBase

import pygame
from pygame.sprite import Group

from ui_components.button import Button
from assets.assets_loader import AssetsLoader
from .screen_base import MAIN_MENU


class MainMenu(ScreenBase):
    def __init__(self, manager, screen_surface: Surface) -> None:
        super().__init__(None, manager, MAIN_MENU)

        self.manager = manager
        self.screen_surface = screen_surface
        self.width, self.height = self.screen_surface.get_size()

        alt = pygame.surface.Surface((200, 100))
        alt.fill((255, 0, 0))

        file = open("data/saved_mazes.json", "r")
        # FIXME: Loading a maze shouldn't be done here.
        #  User should have the option to choose maze to load when pressing the play button
        data = json.load(file)
        self.the_maze_text = UIComponent(image=AssetsLoader.get_text("the_maze"))

        self.play_button = Button(
            image=AssetsLoader.get_button("play_button"),
            alt_image=AssetsLoader.get_button("play_button", hovered=True),
            desired_size=(300, 100),
            position=(self.width // 2, self.height // 2 - 50),
            callback=lambda: self.manager.maze_selection(self, self.manager),
        )
        self.settings_button = Button(
            image=AssetsLoader.get_button("settings_button"),
            alt_image=AssetsLoader.get_button("settings_button", hovered=True),
            desired_size=(550, 100),
            position=(self.width // 2, self.height // 2 + 100),
            callback=lambda: self.manager.options(self, self.manager),
        )
        self.quit_button = Button(
            image=AssetsLoader.get_button("quit_button"),
            alt_image=AssetsLoader.get_button("quit_button", hovered=True),
            desired_size=(150, 50),
            position=(150, self.height - 100),
            callback=lambda: self.manager.back(None),
        )
        self.credits_button = Button(
            image=AssetsLoader.get_button("credits_button"),
            alt_image=AssetsLoader.get_button("credits_button", hovered=True),
            desired_size=(225, 50),
            position=(self.width - 150, self.height - 100),
            callback=lambda: self.manager.credits(self, self.manager),
        )
        self.buttons: Group[Button] = pygame.sprite.Group(
            self.play_button,
            self.settings_button,
            self.quit_button,
            self.credits_button,
        )

    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        self.the_maze_text.draw(
            surface, (self.width // 2 - self.the_maze_text.rect.width // 2, 50)
        )
        # TODO: z jakiegos powodu uzywanie self.buttons.draw sprawia ze one sie nie aktualizuja (readme)
        for button in self.buttons:
            button.draw(surface)

    def update(self, events, keys) -> None:
        for event in events:
            self.buttons.update(event)
