import pygame
from screens import *
from screens.screen_base import *
from maze import Maze
import json


class App:
    def __init__(self, width=1280, heigth=760) -> None:
        pygame.init()
        pygame.font.init()
        self.width = width
        self.heigth = heigth
        self.screens: dict[str, ScreenBase] = {
            MAIN_MENU: MainMenu("Main Menu", self.width, self.heigth),
            PLAY: PlayScreen("Play", self.width, self.heigth),
            OPTIONS: OptionsScreen("Options", self.width, self.heigth),
            GAME: None,
        }
        self.current_screen = self.screens[MAIN_MENU]

    def run(self) -> None:

        pygame.display.set_caption("Main Menu")
        screen = pygame.display.set_mode((self.width, self.heigth))
        clock = pygame.time.Clock()
        running = True
        file = open("data/saved_mazes.json", "r")
        data = json.load(file)
        maze = Maze.from_json(data["Maze1"])
        print(maze)
        while running:
            events = pygame.event.get()
            keys = pygame.key.get_pressed()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            self.current_screen.update(events, keys)
            self.current_screen.draw(screen)
            if self.current_screen.done:
                if self.current_screen.next_screen == GAME:
                    self.screens[GAME] = GameScreen(
                        "Game", self.width, self.heigth, maze
                    )
                self.current_screen = self.screens[self.current_screen.next_screen]
                self.current_screen.makeCurrent()

            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    app = App()
    app.run()