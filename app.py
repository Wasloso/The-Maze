import pygame
from pygame.event import Event
from screens import *
from screens.screen_base import *
from maze import Maze
import json


class App:
    def __init__(self, width=1280, heigth=800) -> None:
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("The Maze")
        self.width = width
        self.heigth = heigth
        self.screen = pygame.display.set_mode((self.width, self.heigth))
        """Dictionary of screens used in app. Main menu, options and play are kindof static - they dont change, but game screen is created when needed."""
        self.screens: dict[str, ScreenBase] = {
            MAIN_MENU: MainMenu("Main Menu", self.width, self.heigth),
            PLAY: PlayScreen("Play", self.width, self.heigth),
            OPTIONS: OptionsScreen("Options", self.width, self.heigth),
            GAME: None,
        }
        self.current_screen = self.screens[MAIN_MENU]
        self.current_screen.makeCurrent()

    def run(self) -> None:

        clock = pygame.time.Clock()
        self.running = True
        file = open("data/saved_mazes.json", "r")
        data = json.load(file)
        maze = Maze.from_json(data["Spiral"])

        while self.running:
            clock.tick(60)
            events = pygame.event.get()
            keys = pygame.key.get_pressed()
            self.handle_events(events, keys)
            if self.current_screen.done:
                if self.current_screen.next_screen == GAME:
                    self.screens[GAME] = GameScreen(
                        "Game", self.width, self.heigth, maze
                    )
                self.current_screen = self.screens[self.current_screen.next_screen]
                self.current_screen.makeCurrent()

            pygame.display.flip()

    def handle_events(self, events: list[Event], keys):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        self.current_screen.update(events, keys)
        self.current_screen.draw(self.screen)


if __name__ == "__main__":
    app = App()
    app.run()
