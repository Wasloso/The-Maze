from pygame.rect import Rect


class Cell:
    def __init__(self, size: int, x: int, y: int, collidable: bool = False) -> None:
        self.rect = Rect(x * size, y * size, size, size)
        self.position = (x, y)
        self.collidable = collidable
        self.size = size

    def change_collidable(self, collidable=False) -> None:
        self.collidable = collidable if collidable else not self.collidable
