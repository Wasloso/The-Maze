from .screen_base import *
import pygame
import sys

sys.path.append("../")
from ui_components.button import Button


class MainMenu(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height)
        play_image = pygame.image.load("assets/button_play.png")
        alt = pygame.surface.Surface((200, 100))
        alt.fill((255, 0, 0))
        self.play_button = Button(
            image=play_image,
            position=(self.width // 2, self.height // 2 + 200),
            callback=self.start_game,
        )

        self.options_button = Button(
            image=play_image,
            position=(self.width // 2, self.height // 2),
            callback=self.start_game,
            altImage=alt,
        )
        self.quit_button = Button(
            image=play_image,
            position=(self.width // 2, self.height // 2 - 200),
            callback=self.start_game,
            altImage=alt,
        )
        self.buttons = pygame.sprite.Group(
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
