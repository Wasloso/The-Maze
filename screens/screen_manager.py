import sys

import pygame

from . import GameScreen, CreditsScreen, SettingsScreen, MazeSelectionScreen, ScreenBase
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
        self.current_screen = GameScreen(previous_screen, manager, maze, ai)

    def credits(self, previous_screen, manager):
        self.current_screen = CreditsScreen(previous_screen, manager)

    def settings(self, previous_screen, manager):
        self.current_screen = SettingsScreen(
            previous_screen, manager, self.settings_manager
        )

    def back(self, previous_screen):
        if previous_screen:
            self.current_screen = previous_screen
        else:
            self.settings_manager.save_settings()
            pygame.quit()
            sys.exit()
