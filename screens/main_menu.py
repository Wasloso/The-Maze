from .screen_base import *
import pygame
from .button import Button


class MainMenu(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height)
        font = pygame.font.Font(None, 36)
        play_image = pygame.image.load("assets/button_play.png")
        self.play_button = Button(
            image=play_image, position=(100, 100), callback=self.start_game
        )
        self.options_button = Button(
            image=play_image, position=(100, 100), callback=self.start_game
        )
        self.quit_button = Button(
            image=play_image, position=(100, 100), callback=self.start_game
        )
        self.buttons = pygame.sprite.Group(
            self.play_button, self.options_button, self.quit_button
        )
        self.selected_maze = None

    def draw(self, screen: pygame.Surface) -> None:
        super(MainMenu, self).draw(screen)
        self.buttons.draw(screen)

    def update(self, events: list, keys) -> None:
        for event in events:
            self.buttons.update(event)

    def makeCurrent(self) -> None:
        super().makeCurrent()

    def start_game(self):
        super().change_screen(GAME)
