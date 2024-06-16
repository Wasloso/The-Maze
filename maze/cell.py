from pygame.rect import Rect


class Cell:
    def __init__(self, x: int, y: int, size: int, collidable: bool = False) -> None:
        self.position = (x, y)
        self.rect = Rect(x * size, y * size, size, size)
        self.collidable = collidable

    def __repr__(self):
        return f"Cell(position:{self.position})"

    def change_collidable(self, collidable=False) -> None:
        self.collidable = collidable if collidable else not self.collidable
