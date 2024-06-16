import json

from maze import Maze


class MazeManager:
    def __init__(self, path="data/saved_mazes.json"):
        self.path = path
        self.mazes = []

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
        mazes = [maze.to_json() for maze in self.mazes]
        with open(self.path, "w") as f:
            # TODO: add better formatting
            data: str = json.dumps({"mazes": mazes}, indent=4)
            data.replace("    ", "\t")
            f.write(data)

    def add_maze(self, maze: Maze) -> None:
        if maze.name is None:
            name = 0
            existing_names = {m.name for m in self.mazes}
            while f"Maze {name}" in existing_names:
                name += 1
            maze.name = f"Maze {name}"
        self.mazes.append(maze)
        self.save_mazes()
