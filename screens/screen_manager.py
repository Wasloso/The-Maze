import sys

import pygame


from . import (
    MazeSelectionScreen,
    GameScreen,
    CreditsScreen,
    SettingsScreen,
    MazeCreatorScreen,
    ScreenBase,
)
from data import SettingsManager


class ScreenManager:
    def __init__(self, settings_manager: SettingsManager):
        self.current_screen: ScreenBase = None
        self.settings_manager: SettingsManager = settings_manager

    def update(self, events, keys):
        if self.current_screen:
            self.current_screen.update(events, keys)

    def draw(self, screen):
        if self.current_screen:
            self.current_screen.draw(screen)

    def load_screen(self, screen):
        self.current_screen = screen

    def maze_selection(self, previous_screen, manager):
        self.current_screen = MazeSelectionScreen(previous_screen, manager)

    def start_game(self, previous_screen, manager, maze, ai=False):
        # FIXME: Create choose ai value
        self.current_screen = GameScreen(previous_screen, manager, maze, False)

    def credits(self, previous_screen, manager):
        self.current_screen = CreditsScreen(previous_screen, manager)

    def settings(self, previous_screen, manager):
        self.current_screen = SettingsScreen(
            previous_screen, manager, self.settings_manager
        )

    def maze_creator(self, previous_screen, manager, maze_manager, maze=None):
        self.current_screen = MazeCreatorScreen(
            previous_screen, manager, maze_manager, maze
        )

    def back(self, previous_screen):
        if previous_screen:
            self.current_screen = previous_screen
        else:
            self.settings_manager.save_settings()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    pass
