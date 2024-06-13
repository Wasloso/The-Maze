import json

from maze.maze import Maze


class MazeManager:
    def __init__(self, path="data/saved_mazes.json"):
        self.path = path
        self.mazes = []

    def load_mazes(self) -> list[Maze]:
        with open(self.path, 'r') as f:
            data = json.load(f)
            if data:
                data = data["mazes"]
                for maze in data:
                    self.mazes.append(Maze.from_json(maze))
        return self.mazes

    def save_mazes(self, mazes: list[Maze]):
        self.mazes = [maze.to_json() for maze in mazes]

        with open(self.path, "w") as f:
            # TODO: add better formatting
            data: str = json.dumps({"mazes": self.mazes}, indent=4)
            data.replace("    ", "\t")
            f.write(data)
