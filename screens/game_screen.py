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
        # player_img = pygame.image.load("assets/player.png")
        self.player = Player(
            self.maze.player_start, 2, size=self.maze.cell_size // 3, image=None
        )
        self.objective = Objective(
            self.maze.objective_position, size=self.maze.cell_size // 3
        )

    def draw(self, screen: Surface) -> None:
        super().draw(screen)
        self.maze.draw(screen)
        self.player.draw(screen)
        self.objective.draw(screen)

    def update(self, events: list, keys) -> None:
        self.handle_buttons_click(keys)
        if self.objective.check_collision(self.player.rect):
            self.done = True
            self.next_screen = "main_menu_screen"
        super().update(events, keys)

    def handle_buttons_click(self, keys):
        multiplier = 2 if keys[pygame.K_LSHIFT] else 1
        if keys[pygame.K_UP]:
            print(pygame.K_UP)
            self.move_player(pygame.K_UP, multiplier)
        if keys[pygame.K_DOWN]:
            self.move_player(pygame.K_DOWN, multiplier)
        if keys[pygame.K_LEFT]:
            self.move_player(pygame.K_LEFT, multiplier)
        if keys[pygame.K_RIGHT]:
            self.move_player(pygame.K_RIGHT, multiplier)

    def move_player(self, direction, multiplier=1):
        print(direction)
        new_rect = self.player.try_move(direction, multiplier)
        if not self.maze.check_collision(new_rect):
            self.player.rect = new_rect

    def makeCurrent(self) -> None:
        pass
