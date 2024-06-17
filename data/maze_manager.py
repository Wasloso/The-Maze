import json
from maze import Maze


class MazeManager:
    def __init__(self, path: str = "data/saved_mazes.json") -> None:
        self.path: str = path
        self.mazes: list[Maze] = []

    def load_mazes(self) -> None:
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
                if data:
                    self.mazes = [Maze.from_json(maze) for maze in data["mazes"]]
        except FileNotFoundError:
            self.mazes = []
            self.save_mazes()

    def save_mazes(self) -> None:
        with open(self.path, "w") as f:
            data: str = json.dumps(
                {"mazes": [maze.to_json() for maze in self.mazes]}, indent=4
            )
            data.replace("    ", "\t")
            f.write(data)

    def add_maze(self, maze: Maze) -> None:
        if not maze.name:
            name = 0
            while f"Maze {name}" in {m.name for m in self.mazes}:
                name += 1
            maze.name = f"Maze {name}"
        self.mazes.append(maze)
        self.save_mazes()
