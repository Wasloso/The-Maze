from .screen_base import *
import pygame
from pygame.sprite import Group
import sys

sys.path.append("../")
from ui_components.button import Button
from ui_components.volume_controller import VolumeController
from assets.assets_loader import AssetsLoader


class MainMenu(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height, screenName=MAIN_MENU)
        alt = pygame.surface.Surface((200, 100))
        alt.fill((255, 0, 0))
        self.play_button = Button(
            image=AssetsLoader.get_button("play_button"),
            position=(self.width // 2, self.height // 2 - 50),
            callback=self.start_game,
        )
        self.settings_button = Button(
            image=AssetsLoader.get_button("setting_button"),
            position=(self.width // 2, self.height // 2 + 100),
            callback=self.open_options,
            altImage=alt,
        )
        self.exit_button = Button(
            image=AssetsLoader.get_button("exit_button"),
            position=(150, self.height - 100),
            altImage=alt,
        )
        self.credits_button = Button(
            image=AssetsLoader.get_button("credits_button"),
            position=(self.width - 150, self.height - 100),
            altImage=alt,
        )
        self.buttons: Group[Button] = pygame.sprite.Group(
            self.play_button,
            self.settings_button,
            self.exit_button,
            self.credits_button,
        )
        self.selected_maze = None

    def draw(self, screen: pygame.Surface) -> None:
        super().draw(screen)
        # TODO: z jakiegos powodu uzywanie self.buttons.draw sprawia ze one sie nie aktualizuja (readme)
        for button in self.buttons:
            button.draw(screen)

    def update(self, events, keys) -> None:
        for event in events:
            self.buttons.update(event)

    def makeCurrent(self) -> None:
        super().makeCurrent()

    def start_game(self):
        super().change_screen(GAME)

    def open_options(self):
        super().change_screen(OPTIONS)
