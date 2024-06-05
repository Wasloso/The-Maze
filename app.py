import pygame
from screens import *
from maze import Maze


class App:
    def __init__(self, width=800, heigth=600) -> None:
        maze = Maze(50, 20, 20)
        maze.randomize_maze()
        self.width = width
        self.heigth = heigth
        self.screens: dict[str, ScreenBase] = {
            "main_menu": MainMenu("Main Menu", self.width, self.heigth),
            "play": PlayScreen("Play", self.width, self.heigth),
            "options": OptionsScreen("Options", self.width, self.heigth),
            "game": GameScreen("Game", self.width, self.heigth, maze),
        }
        self.current_screen = self.screens["game"]

    def run(self) -> None:
        pygame.init()
        pygame.display.set_caption("Main Menu")
        screen = pygame.display.set_mode((self.width, self.heigth))
        clock = pygame.time.Clock()
        running = True

        while running:
            events = pygame.event.get()
            keys = pygame.key.get_pressed()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            self.current_screen.update(events, keys)
            self.current_screen.draw(screen)

            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    app = App()
    app.run()
