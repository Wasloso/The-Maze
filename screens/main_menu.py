from .screen_base import *
import pygame
from .button import Button


class MainMenu(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height)
        font = pygame.font.Font(None, 36)
        play_image = pygame.image.load("assets/button_play.png")
        alt = pygame.surface.Surface((200, 100))
        alt.fill((255, 0, 0))
        self.play_button = Button(
            image=play_image,
            position=(self.width // 2, self.height // 2),
            callback=self.start_game,
        )

        # self.options_button = Button(
        #     image=play_image,
        #     position=(100, 100),
        #     callback=self.start_game,
        #     altImage=alt,
        # )
        # self.quit_button = Button(
        #     image=play_image,
        #     position=(100, 100),
        #     callback=self.start_game,
        #     altImage=alt,
        # )
        self.buttons = pygame.sprite.Group(self.play_button)
        self.selected_maze = None

    def draw(self, screen: pygame.Surface) -> None:
        super(MainMenu, self).draw(screen)
        # Musi byc tak zamiast self.buttons.draw(screen) bo inaczej nie dziala on hover image
        for button in self.buttons:
            button.draw(screen)

    def update(self, events, keys) -> None:
        for event in events:
            self.buttons.update(event)

    def makeCurrent(self) -> None:
        super().makeCurrent()

    def start_game(self):
        super().change_screen(GAME)
