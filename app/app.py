import sys

import pygame
import pygame.key
from pygame.event import Event
from data import SettingsManager
from screens import ScreenManager, MainMenu


class App:
    def __init__(self, width: int = 1280, height: int = 800) -> None:
        self.width: int = width
        self.height: int = height

        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("The Maze")

    def run(self) -> None:
        # Initializing display and necessary screens
        setting_manager: SettingsManager = SettingsManager()
        setting_manager.load_settings()
        screen_manager: ScreenManager = ScreenManager(setting_manager)

        surface = pygame.display.set_mode((self.width, self.height))
        screen_manager.load_screen(MainMenu(screen_manager, surface))

        clock = pygame.time.Clock()
        while True:
            events, keys = pygame.event.get(), pygame.key.get_pressed()

            for event in events:
                if event.type == pygame.QUIT:
                    setting_manager.save_settings()
                    pygame.quit()
                    sys.exit()

            screen_manager.update(events, keys)
            screen_manager.draw(surface)

            pygame.display.flip()
            clock.tick(60)


def main():
    App().run()


if __name__ == "__main__":
    main()
