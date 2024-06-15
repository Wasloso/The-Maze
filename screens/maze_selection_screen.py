from .screen_base import *
from typing import Optional
from pygame.surface import Surface
from pygame import Surface
from ui_components.button import Button
from data import MazeManager


class MazeSelectionScreen(ScreenBase):
    def __init__(self, previous_screen: Optional[ScreenBase], manager) -> None:
        super().__init__(previous_screen, manager, screen_name=MAZE_SELECTION)
        self.back_button = Button.go_back_button(
            position=(50, 50), callback=lambda: self.manager.back(previous_screen)
        )
        self.buttons: list[Button] = []
        self.mazes = MazeManager().load_mazes()
        for maze in self.mazes:
            self.buttons.append(
                Button(
                    image=AssetsLoader.get_button("play_button"),
                    alt_image=AssetsLoader.get_button("play_button", hovered=True),
                    desired_size=(300, 100),
                    callback=lambda m=maze: self.manager.start_game(
                        self, self.manager, m
                    ),
                )
            )

        self.add_maze_button = Button(
            image=AssetsLoader.get_button("add_maze_button"),
            alt_image=AssetsLoader.get_button("add_maze_button", hovered=True),
            desired_size=(50, 50),
            callback=lambda: self.manager.maze_creator(
                self, self.manager, self.mazes[0]
            ),
        )

    def draw(self, surface: Surface) -> None:
        super().draw(surface)
        self.back_button.draw(surface)
        for i, button in enumerate(self.buttons):
            button.draw(surface, (50, 150 + i * 150))

        self.add_maze_button.draw(
            surface, (surface.get_width() // 2, surface.get_height() - 100)
        )

    def update(self, events, keys) -> None:
        super().update(events, keys)
        for event in events:
            self.back_button.update(event)
            self.add_maze_button.update(event)
            for button in self.buttons:
                button.update(event)
