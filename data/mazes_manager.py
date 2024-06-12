from .file_loader import FileManager
import sys

sys.path.append("./")
from maze.maze import Maze


class MazesManager:
    def __init__(self, path="data/saved_mazes.json"):
        self.loader = FileManager("data/saved_mazes.json")
        self.mazes = []

    def load_mazes(self) -> list[Maze]:
        data = self.loader.load()["mazes"]
        for maze in data:
            self.mazes.append(Maze.from_json(maze))
        return self.mazes

    def save_mazes(self, mazes: list[Maze]):
        self.mazes = [maze.to_json() for maze in mazes]
        self.loader.save({"mazes": self.mazes})


if __name__ == "__main__":
    manager = MazesManager()
    mazes = manager.load_mazes()
    m = []
    for maze in mazes:
        m.append(maze.to_json())

    manager.save_mazes(mazes)
