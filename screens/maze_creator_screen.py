from . import ScreenBase
from .screen_base import MAZE_CREATOR, MAZE_SELECTION
from maze.maze import Maze
from maze.cell import Cell
from pygame.surface import Surface
from typing import Optional
from ui_components.button import Button
from assets.assets_loader import AssetsLoader
import pygame


class MazeCreatorScreen(ScreenBase):
    def __init__(
        self,
        previous_screen: Optional[ScreenBase],
        manager,
        maze: Maze = None,
    ) -> None:
        super().__init__(previous_screen, manager, screen_name=MAZE_CREATOR)
        if maze is None:
            maze = Maze(40)
            maze.create_grid()
        self.maze: Maze = maze
        transparent_surf = Surface(
            (self.maze.cell_size, self.maze.cell_size), pygame.SRCALPHA
        )
        transparent_surf.fill((0, 0, 0, 0))
        self.wall_img = pygame.transform.scale(
            AssetsLoader.get_cell("wall"), (self.maze.cell_size, self.maze.cell_size)
        )
        self.floor_img = pygame.transform.scale(
            AssetsLoader.get_cell("floor"), (self.maze.cell_size, self.maze.cell_size)
        )

        self.back_button = Button.go_back_button(
            desired_size=(50, 50),
            position=(25, 25),
            callback=lambda: self.manager.back(previous_screen),
        )
        self.cell_buttons = []
        self.cells = []
        for i, row in enumerate(self.maze.grid):
            cell: Cell
            for j, cell in enumerate(row):
                self.cells.append(cell)
                self.cell_buttons.append(
                    Button(
                        image=transparent_surf,
                        position=cell.rect.center,
                        desired_size=(self.maze.cell_size, self.maze.cell_size),
                        callback=(
                            (lambda c=cell: c.change_collidable())
                            if i != 0
                            and i != len(self.maze.grid) - 1
                            and j != 0
                            and j != len(row) - 1
                            else None
                        ),
                    )
                )

    def draw(self, surface: Surface) -> None:
        super().draw(surface)
        for cell in self.cells:
            if cell.collidable:
                surface.blit(self.wall_img, cell.rect.topleft)
            else:
                surface.blit(self.floor_img, cell.rect.topleft)
        for button in self.cell_buttons:
            button.draw(surface)
        self.back_button.draw(surface)

    def update(self, events, keys) -> None:
        for event in events:
            self.back_button.update(event)
            for button in self.cell_buttons:
                button.update(event)

    def toggle_collidable(self, cell: Cell): ...
