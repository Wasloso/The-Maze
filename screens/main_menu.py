import json

from pygame import Surface

from .screen_base import *
import pygame
from pygame.sprite import Group

from ui_components.button import Button
from assets.assets_loader import AssetsLoader


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
        from maze import Maze
        maze = Maze.from_json(data["Spiral"])
        self.play_button = Button(
            image=AssetsLoader.get_button("play_button"),
            position=(self.width // 2, self.height // 2 - 50),
            callback=lambda: self.manager.start_game(self, self.manager, maze),
        )
        self.settings_button = Button(
            image=AssetsLoader.get_button("setting_button"),
            position=(self.width // 2, self.height // 2 + 100),
            callback=lambda: self.manager.options(self, self.manager),
            altImage=alt,
        )
        self.exit_button = Button(
            image=AssetsLoader.get_button("exit_button"),
            position=(150, self.height - 100),
            altImage=alt,
            callback=lambda: self.manager.back(None),
        )
        self.credits_button = Button(
            image=AssetsLoader.get_button("credits_button"),
            position=(self.width - 150, self.height - 100),
            altImage=alt,
            callback=lambda: self.manager.credits(self, self.manager),
        )
        self.buttons: Group[Button] = pygame.sprite.Group(
            self.play_button,
            self.settings_button,
            self.exit_button,
            self.credits_button,
        )
        self.selected_maze = None

    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        # TODO: z jakiegos powodu uzywanie self.buttons.draw sprawia ze one sie nie aktualizuja (readme)
        for button in self.buttons:
            button.draw(surface)

    def update(self, events, keys) -> None:
        for event in events:
            self.buttons.update(event)

    def open_options(self):
        super().change_screen(OPTIONS, self.screen_surface)
