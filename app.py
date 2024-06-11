import sys

import pygame.key
from pygame.event import Event

from screens import MainMenu, ScreenManager


class App:
    screen_manager: ScreenManager = None
    screen = None

    def __init__(self, width: int = 1280, height: int = 800) -> None:
        self.width: int = width
        self.height: int = height

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("The Maze")

    def run(self) -> None:
        # Initializing display and necessary screens
        screen_manager = ScreenManager()

        surface = pygame.display.set_mode((self.width, self.height))
        screen_manager.load_screen(MainMenu(screen_manager, surface))

        clock = pygame.time.Clock()

        # FIXME: Loading a maze shouldn't be done here.
        #  User should have the option to choose maze to load when pressing the play button
        # file = open("data/saved_mazes.json", "r")
        # data = json.load(file)
        # maze = Maze.from_json(data["Spiral"])

        while True:
            events, keys = pygame.event.get(), pygame.key.get_pressed()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen_manager.update(events, keys)
            screen_manager.draw(surface)

            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    App().run()
