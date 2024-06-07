from .screen_base import *
import pygame
from pygame.sprite import Group
import sys

sys.path.append("../")
from ui_components.button import Button
from ui_components.volume_controller import VolumeController


class MainMenu(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height, screenName=MAIN_MENU)
        play_image = pygame.image.load("assets/buttons/button_play.png")
        alt = pygame.surface.Surface((200, 100))
        alt.fill((255, 0, 0))
        self.play_button = Button(
            image=play_image,
            position=(self.width // 2, self.height // 2 - 200),
            callback=self.start_game,
        )
        options_image = pygame.image.load("assets/buttons/placeholder.png")
        self.options_button = Button(
            image=options_image,
            position=(self.width // 2, self.height // 2),
            callback=self.open_options,
            altImage=alt,
        )
        quit_image = pygame.image.load("assets/buttons/placeholder.png")
        self.quit_button = Button(
            image=quit_image,
            position=(self.width // 2, self.height // 2 + 200),
            callback=self.start_game,
            altImage=alt,
        )
        self.buttons: Group[Button] = pygame.sprite.Group(
            self.play_button, self.options_button, self.quit_button
        )
        self.selected_maze = None

    def draw(self, screen: pygame.Surface) -> None:
        super().draw(screen)
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
