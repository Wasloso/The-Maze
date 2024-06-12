import json


class FileManager:
    def __init__(self, path):
        self.path = path

    def load(self) -> dict:
        with open(self.path) as f:
            return json.load(f)

    def save(self, data: dict):
        with open(self.path, "w") as f:
            # TODO: add better formatting
            data: str = json.dumps(data, indent=4)
            data.replace("    ", "\t")

            f.write(data)
