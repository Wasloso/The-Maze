import sys
from pygame.surface import Surface
import pygame

sys.path.append("../")

from screens.screen_base import ScreenBase
from maze.maze import Maze
from maze.player import Player
from maze.objective import Objective


class GameScreen(ScreenBase):
    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        maze: Maze,
        ai: bool = False,
    ) -> None:
        super().__init__(title, width, height)
        self.maze = maze
        self.ai = ai
        self.player = Player(self.maze.player_start, 2)
        self.objective = Objective(self.maze.objective_position)

    def draw(self, screen: Surface) -> None:
        screen.fill((0, 0, 0))
        self.maze.draw(screen)
        self.player.draw(screen)
        self.objective.draw(screen)

    def update(self, events: list, keys) -> None:
        if keys[pygame.K_UP]:
            new_rect = self.player.try_move(0, -1)
            if not self.maze.check_collision(new_rect):
                self.player.rect = new_rect
        if keys[pygame.K_DOWN]:
            new_rect = self.player.try_move(0, 1)
            if not self.maze.check_collision(new_rect):
                self.player.rect = new_rect

        if keys[pygame.K_LEFT]:
            new_rect = self.player.try_move(-1, 0)

            if not self.maze.check_collision(new_rect):
                self.player.rect = new_rect

        if keys[pygame.K_RIGHT]:
            new_rect = self.player.try_move(1, 0)

            if not self.maze.check_collision(new_rect):
                self.player.rect = new_rect

        if self.objective.check_collision(self.player.rect):
            self.done = True
            self.next_screen = "main_menu_screen"

    def makeCurrent(self) -> None:
        pass
