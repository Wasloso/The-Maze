import json

from maze.maze import Maze


class MazeManager:
    def __init__(self, path="data/saved_mazes.json"):
        self.path = path
        self.mazes = []

    def load_mazes(self) -> list[Maze]:
        with open(self.path, "r") as f:
            data = json.load(f)
            if data:
                data = data["mazes"]
                self.mazes = [Maze.from_json(maze) for maze in data]
        return self.mazes

    def save_mazes(self):
        mazes = [maze.to_json() for maze in self.mazes]

        with open(self.path, "w") as f:
            # TODO: add better formatting
            data: str = json.dumps({"mazes": mazes}, indent=4)
            data.replace("    ", "\t")
            f.write(data)

    def add_maze(self, maze):
        if maze.name is None:
            name = 0
            while any(m.name == name for m in self.mazes):
                name += 1
            maze.name = f"Maze {name}"
        self.mazes.append(maze)
        self.save_mazes()
