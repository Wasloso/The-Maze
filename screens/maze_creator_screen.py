from . import ScreenBase
from .screen_base import MAZE_CREATOR, MAZE_SELECTION, MAIN_MENU
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
        maze_manager,
        maze: Maze = None,
    ) -> None:
        super().__init__(previous_screen, manager, screen_name=MAZE_CREATOR)
        self.player_img = AssetsLoader.get_player("idle")
        self.objective_img = AssetsLoader.get_objective()
        self.maze_manager = maze_manager
        self.maze: Maze = maze
        self.confirm_button = Button(
            desired_size=(50, 50),
            position=(25, 25),
            image=AssetsLoader.get_button("confirm_button"),
            alt_image=AssetsLoader.get_button("confirm_button", hovered=True),
            callback=(
                (lambda m=self.maze: self.add_maze())
                if maze is None
                else lambda: self.manager.back(previous_screen)
            ),
        )
        if maze is None:
            maze = Maze(40)
            maze.create_grid()
            self.maze = maze

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
        self.confirm_button.draw(surface)

        if self.maze.player_start:
            surface.blit(
                self.player_img,
                self.maze.player_start,
            )
        if self.maze.objective_position:
            surface.blit(
                self.objective_img,
                self.maze.objective_position,
            )

    def update(self, events, keys) -> None:
        for event in events:
            self.confirm_button.update(event)
            for button in self.cell_buttons:
                button.update(event)
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == pygame.BUTTON_RIGHT
            ):
                pos = pygame.mouse.get_pos()
                grid_pos = self.maze.get_rect_pos_in_grid(*pos)
                objective_pos = (
                    self.maze.get_rect_pos_in_grid(*self.maze.objective_position)
                    if self.maze.objective_position
                    else None
                )
                player_pos = (
                    self.maze.get_rect_pos_in_grid(*self.maze.player_start)
                    if self.maze.player_start
                    else None
                )

                if keys[pygame.K_LSHIFT] and grid_pos != player_pos:
                    self.maze.objective_position = pos
                elif grid_pos != objective_pos:
                    self.maze.player_start = pos

    def toggle_collidable(self, cell: Cell): ...

    def add_maze(self):
        self.maze_manager.add_maze(self.maze)
        self.previous_screen.reload()
        self.manager.back(self.previous_screen)
