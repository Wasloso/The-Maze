import math
from .cell import Cell
import random
from pygame import Surface
import json
import ast


class Maze:
    def __init__(
        self,
        cell_size: int,
        rows: int = 20,
        columns: int = 15,
        player_start: tuple[int, int] = (0, 0),
        objective_position: tuple[int, int] = (100, 100),
    ):
        self.rows: int = rows
        self.columns: int = columns
        self.cell_size: int = cell_size
        self.collidable_cells: list[Cell] = []
        self.player_start = player_start
        self.objective_position = objective_position
        self.grid: list[list[Cell]] = None

    def create_grid(self) -> list[list[Cell]]:
        grid = []
        self.collidable_cells.clear()
        for y in range(self.columns):
            row = []
            for x in range(self.rows):
                cell = Cell(
                    self.cell_size, x * self.cell_size, y * self.cell_size, True
                )
                self.collidable_cells.append(cell)
                row.append(cell)
            grid.append(row)
        return grid

    def draw(self, screen: Surface):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)

    def check_collision(self, rect):
        for cell in self.collidable_cells:
            if cell.rect.colliderect(rect):
                return True
        return False

    def randomize_maze(self):
        self.collidable_cells.clear()
        for row in self.grid:
            for cell in row:
                if random.random() < 0.2:
                    cell.change_collidable(True)
                    self.collidable_cells.append(cell)

    def __repr__(self):
        return f"Maze({self.grid=}, {self.cell_size=}, {self.rows=}, {self.columns=}, {self.player_start=}, {self.objective_position=})"

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
        maze = Maze(json["cell_size"], rows, columns)
        maze.player_start = ast.literal_eval(json["player_start"])
        maze.objective_position = ast.literal_eval(json["objective_position"])
        maze.grid = []
        for j, row in enumerate(grid):
            maze_row = []
            for i, cell in enumerate(row):
                if cell == 1:
                    cell = Cell(
                        maze.cell_size, i * maze.cell_size, j * maze.cell_size, True
                    )
                    maze_row.append(cell)
                    maze.collidable_cells.append(cell)
                else:
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
