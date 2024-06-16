from __future__ import annotations
import random

from maze import Cell


class Maze:
    def __init__(
        self,
        cell_size: int,
        rows: int = 20,
        columns: int = 32,
        player_start: tuple[int, int] = None,
        objective_position: tuple[int, int] = None,
        name: str = None,
    ):
        self.rows: int = rows
        self.columns: int = columns
        self.cell_size: int = cell_size
        self.player_start = player_start
        self.objective_position = objective_position
        self.grid: list[list[Cell]] = []
        self.name = name
        self.player_start_pos = None
        self.objective_position_pos = None

    def create_grid(self) -> list[list[Cell]]:
        grid = []
        for y in range(self.rows):
            row = []
            for x in range(self.columns):
                cell = Cell(x, y, self.cell_size, True)
                row.append(cell)
            grid.append(row)
        self.grid = grid
        return grid

    def randomize_maze(self) -> None:
        non_collidable_cells: list[Cell] = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if (i == 0 or j == 0) or (i == self.rows - 1 or j == self.columns - 1):
                    cell.collidable = True
                elif random.random() < 0.7:
                    cell.collidable = True
                else:
                    non_collidable_cells.append(cell)
                    cell.collidable = False
        self.player_start = random.choice(non_collidable_cells).rect.center
        while self.player_start == self.objective_position:
            self.objective_position = random.choice(non_collidable_cells).rect.center

    def __repr__(self) -> str:
        return f"Maze({self.cell_size=}, {self.rows=}, {self.columns=}, {self.player_start=}, {self.objective_position=}, {self.name=})"

    @staticmethod
    def from_json(json) -> Maze:
        grid = json["grid"]

        maze = Maze(json["cell_size"], len(grid[0]), len(grid), name=json["name"])
        for i, row in enumerate(grid):
            maze_row = []
            for j, cell in enumerate(row):
                collidable: bool = cell
                if cell == "P":
                    maze.player_start_pos = (i, j)
                    maze.player_start = maze.get_rect_position(i, j)
                    collidable = False
                if cell == "O":
                    maze.objective_position_pos = (i, j)
                    maze.objective_position = maze.get_rect_position(i, j)
                    collidable = False

                maze_row.append(Cell(j, i, maze.cell_size, collidable))
            maze.grid.append(maze_row)
        return maze

    def to_json(self) -> dict:
        player_pos = self.get_cell_index(*self.player_start)
        objective_pos = self.get_cell_index(*self.objective_position)
        grid = []
        for row in self.grid:
            grid_row = []
            for cell in row:
                if (
                    row.index(cell) == player_pos[0]
                    and self.grid.index(row) == player_pos[1]
                ):
                    grid_row.append("P")

                elif (
                    row.index(cell) == objective_pos[0]
                    and self.grid.index(row) == objective_pos[1]
                ):
                    grid_row.append("O")
                elif cell.collidable:
                    grid_row.append(1)
                else:
                    grid_row.append(0)
            grid.append(grid_row)
        return {
            "name": self.name,
            "cell_size": self.cell_size,
            "grid": grid,
        }

    def get_cell_index(self, x, y) -> tuple[int, int]:
        return x // self.cell_size, y // self.cell_size

    def get_rect_position(self, row, column) -> tuple[int, int]:
        return (
            column * self.cell_size + self.cell_size // 2,
            row * self.cell_size + self.cell_size // 2,
        )

    def reset_visibility(self) -> None:
        for row in self.grid:
            for cell in row:
                cell.visited = False
