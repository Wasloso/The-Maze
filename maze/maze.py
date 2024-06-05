from .cell import Cell
import random
from pygame import Surface


class Maze:
    def __init__(
        self,
        cell_size: int,
        rows: int,
        columns: int,
        player_start: tuple[int, int] = (0, 0),
        objective_position: tuple[int, int] = (100, 100),
    ):
        self.rows: int = rows
        self.columns: int = columns
        self.cell_size: int = cell_size
        self.collidable_cells: list[Cell] = []
        self.player_start = player_start
        self.objective_position = objective_position
        self.grid: list[list[Cell]] = self.create_grid()

    def create_grid(self) -> list[list[Cell]]:
        grid = []
        self.collidable_cells.clear()
        for y in range(self.columns):
            row = []
            for x in range(self.rows):
                row.append(Cell(self.cell_size, x * self.cell_size, y * self.cell_size))
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

    def generate_maze(self):
        self.collidable_cells.clear()
        self.grid = self.create_grid()

    def __repr__(self):
        return f"Maze({self.grid})"
