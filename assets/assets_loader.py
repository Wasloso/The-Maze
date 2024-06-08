from typing import Any
from pygame.image import load
from pygame.surface import Surface


# I think it can be done better
class AssetsLoader:
    _dir = "assets/"
    _backgroundDir = _dir + "backgrounds/"
    _buttonDir = _dir + "buttons/"
    _playerDir = _dir + "player/"

    paths = {
        "background": {
            "main_menu_screen": _backgroundDir + "main_menu_screen.png",
            "play_screen": _backgroundDir + "play_screen.png",
            "options_screen": _backgroundDir + "options_screen.png",
            "game_screen": _backgroundDir + "game_screen.png",
        },
        "button": {
            "play_button": _buttonDir + "play_button.png",
            "options_button": _buttonDir + "options_button.png",
            "exit_button": _buttonDir + "exit_button.png",
            "back_button": _buttonDir + "back_button.png",
        },
        "player": {
            "idle": _playerDir + "idle.png",
            "walk_UP": _playerDir + "walk_UP.png",
            "walk_DOWN": _playerDir + "walk_DOWN.png",
            "walk_LEFT": _playerDir + "walk_LEFT.png",
            "walk_RIGHT": _playerDir + "walk_RIGHT.png",
        },
        "objective": "assets/objective.png",
        "maze": {
            "wall": "assets/maze/wall.png",
            "floor": "assets/maze/floor.png",
        },
    }

    @staticmethod
    def get_image(category: str, name: str) -> Surface:
        try:
            path = AssetsLoader.paths[category][name]
            return load(path)
        except (KeyError, FileNotFoundError):
            print(f"Missing image: {category}/{name}")
            return load("assets/missing.png")

    @classmethod
    def get_background(cls, name: str) -> Surface:
        return cls.get_image("background", name)

    @classmethod
    def get_button(cls, name: str) -> Surface:
        return cls.get_image("button", name)

    @classmethod
    def get_player(cls, name: str) -> Surface:
        return cls.get_image("player", name)

    @classmethod
    def get_maze(cls, name: str) -> Surface:
        return cls.get_image("maze", name)

    @classmethod
    def get_objective(cls) -> Surface:
        return load(cls.paths["objective"])
