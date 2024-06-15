import math
from .cell import Cell
import random
from pygame import Surface
import json
import ast


class Maze:
    collidable_cells = None

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
        self.grid: list[list[Cell]] = None
        self.name = name

    def create_grid(self) -> list[list[Cell]]:
        grid = []
        for y in range(self.rows):
            row = []
            for x in range(self.columns):
                cell = Cell(
                    self.cell_size, x * self.cell_size, y * self.cell_size, True
                )
                row.append(cell)
            grid.append(row)
        self.grid = grid
        return grid

    def randomize_maze(self):
        for row in self.grid:
            for cell in row:
                if random.random() < 0.2:
                    cell.change_collidable(True)

    def __repr__(self):
        return f"Maze({self.grid=}, {self.cell_size=}, {self.rows=}, {self.columns=}, {self.player_start=}, {self.objective_position=}, {self.name=})"

    # TODO jakas fajna metoda generowania losowego labiryntu
    @staticmethod
    def generate_maze(cell_size, rows, columns):
        maze = Maze(cell_size, rows, columns)
        maze.grid = maze.create_grid()

        player_start = (
            random.randint(1, rows - 2) * cell_size + cell_size // 2,
            random.randint(1, columns - 2) * cell_size + cell_size // 2,
        )
        maze.player_start = player_start
        objective_position = (
            random.randint(1, rows - 2) * cell_size + cell_size // 2,
            random.randint(1, columns - 2) * cell_size + cell_size // 2,
        )
        maze.objective_position = objective_position
        cp, rp = player_start[0] // cell_size, player_start[1] // cell_size
        maze.change_collidable(cp, rp)
        co, ro = objective_position[0] // cell_size, objective_position[1] // cell_size
        maze.change_collidable(co, ro)
        return maze

    def change_collidable(self, column, row):
        self.grid[row][column].change_collidable()
        if self.grid[row][column].collidable:
            self.collidable_cells.append(self.grid[row][column])
        else:
            self.collidable_cells.remove(self.grid[row][column])

    @staticmethod
    def from_json(json):
        grid = json["grid"]
        columns = len(grid)
        rows = len(grid[0])
        name = json["name"]
        maze = Maze(json["cell_size"], rows, columns, name=name)
        maze.grid = []
        for j, row in enumerate(grid):
            maze_row = []
            for i, cell in enumerate(row):
                if cell == 1:
                    cell = Cell(
                        maze.cell_size, i * maze.cell_size, j * maze.cell_size, True
                    )
                    maze_row.append(cell)
                else:
                    if cell == "P":
                        maze.player_start = maze.set_rect_position(j, i)
                    elif cell == "O":
                        maze.objective_position = maze.set_rect_position(j, i)
                    maze_row.append(
                        Cell(
                            maze.cell_size,
                            i * maze.cell_size,
                            j * maze.cell_size,
                            False,
                        )
                    )
            maze.grid.append(maze_row)
        return maze

    def to_json(self) -> dict:
        player_pos = self.get_rect_pos_in_grid(*self.player_start)
        objective_pos = self.get_rect_pos_in_grid(*self.objective_position)
        print(player_pos, objective_pos)
        grid = []
        for row in self.grid:
            grid_row = []
            for cell in row:
                if cell.collidable:
                    grid_row.append(1)
                elif (
                    row.index(cell) == player_pos[0]
                    and self.grid.index(row) == player_pos[1]
                ):
                    grid_row.append("P")
                elif (
                    row.index(cell) == objective_pos[0]
                    and self.grid.index(row) == objective_pos[1]
                ):
                    grid_row.append("O")
                else:
                    grid_row.append(0)
            grid.append(grid_row)
        return {
            "name": self.name,
            "cell_size": self.cell_size,
            "grid": grid,
        }

    def get_rect_pos_in_grid(self, x, y):
        return x // self.cell_size, y // self.cell_size

    def set_rect_position(self, row, column):
        return (
            column * self.cell_size + self.cell_size // 2,
            row * self.cell_size + self.cell_size // 2,
        )
