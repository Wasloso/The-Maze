import json


class FileManager:
    def __init__(self, path: str) -> None:
        self.path: str = path

    def load(self) -> dict:
        with open(self.path) as f:
            return json.load(f)

    def save(self, data: dict) -> None:
        with open(self.path, "w") as f:
            # TODO: add better formatting
            data: str = json.dumps(data, indent=4)
            data.replace("    ", "\t")
            f.write(data)
