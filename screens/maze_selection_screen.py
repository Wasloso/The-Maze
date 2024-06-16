from .screen_base import *
from typing import Optional
from pygame.surface import Surface
from pygame import Surface
from ui_components.button import Button
from data import MazeManager


class MazeSelectionScreen(ScreenBase):
    def __init__(self, previous_screen: Optional[ScreenBase], manager) -> None:
        super().__init__(previous_screen, manager, screen_name=MAZE_SELECTION)

        self.buttons: list[Button] = []
        self.maze_manager = MazeManager()
        self.maze_manager.load_mazes()
        self.selected_maze = None
        self.scroll_offset = 0
        self.scroll_max = 0

        self.add_buttons()

        self.back_button = Button.go_back_button(
            position=(50, 50), callback=lambda: self.back(previous_screen)
        )

        action_buttons_size = (100, 100)

        self.play_maze_button = Button(
            image=AssetsLoader.get_button("run_button"),
            alt_image=AssetsLoader.get_button("run_button", hovered=True),
            desired_size=action_buttons_size,
            callback=lambda: (
                self.manager.start_game(self, self.manager, self.selected_maze)
                if self.selected_maze
                else None
            ),
        )

        self.play_ai_button = Button(
            image=AssetsLoader.get_button("run_ai_button"),
            alt_image=AssetsLoader.get_button("run_ai_button", hovered=True),
            desired_size=action_buttons_size,
            callback=lambda: (
                self.manager.start_game(self, self.manager, self.selected_maze, ai=True)
                if self.selected_maze
                else None
            ),
        )

        self.add_maze_button = Button(
            image=AssetsLoader.get_button("add_button"),
            alt_image=AssetsLoader.get_button("add_button", hovered=True),
            desired_size=action_buttons_size,
            callback=lambda: self.manager.maze_creator(
                self, self.manager, self.maze_manager
            ),
        )
        self.edit_maze_button = Button(
            image=AssetsLoader.get_button("edit_button"),
            alt_image=AssetsLoader.get_button("edit_button", hovered=True),
            desired_size=action_buttons_size,
            callback=lambda: (
                self.manager.maze_creator(
                    self, self.manager, self.maze_manager, self.selected_maze
                )
                if self.selected_maze
                else None
            ),
        )
        self.delete_maze_button = Button(
            image=AssetsLoader.get_button("delete_button"),
            alt_image=AssetsLoader.get_button("delete_button", hovered=True),
            desired_size=action_buttons_size,
            callback=lambda: (
                self.delete_maze(self.selected_maze) if self.selected_maze else None
            ),
        )
        self.action_buttons = [
            self.play_maze_button,
            self.play_ai_button,
            self.edit_maze_button,
            self.delete_maze_button,
            self.add_maze_button,
        ]

    def draw(self, surface: Surface) -> None:
        super().draw(surface)
        self.back_button.draw(surface)
        for i, button in enumerate(self.buttons):
            button.draw(
                surface,
                (
                    50 + (i * button.rect.width + 30) - self.scroll_offset,
                    surface.get_height() // 2 - button.rect.height // 2,
                ),
            )

        for i, button in enumerate(self.action_buttons):
            button.draw(
                surface,
                (
                    surface.get_width() // 2 - 50 * len(self.action_buttons) + 125 * i,
                    surface.get_height() - 150,
                ),
            )

    def add_buttons(self):
        self.buttons.clear()
        for maze in self.maze_manager.mazes:
            self.buttons.append(
                Button(
                    image=AssetsLoader.get_button("play_button"),
                    alt_image=AssetsLoader.get_button("play_button", hovered=True),
                    desired_size=(300, 100),
                    callback=lambda m=maze: self.select_maze(m),
                )
            )
        total_width = len(self.buttons) * (self.buttons[0].rect.width + 30)
        self.scroll_max = max(0, total_width - 1280)
        self.scroll_offset = max(self.scroll_offset, 0)

    def update(self, events, keys) -> None:
        super().update(events, keys)
        for event in events:
            self.back_button.update(event)
            for button in [*self.buttons, *self.action_buttons]:
                button.update(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.scroll_offset = max(self.scroll_offset - 10, 0)
                elif event.button == 5:
                    self.scroll_offset = min(self.scroll_offset + 10, self.scroll_max)

    def select_maze(self, maze):
        self.selected_maze = maze

    def delete_maze(self, maze):
        self.maze_manager.mazes.remove(maze)
        self.maze_manager.save_mazes()
        self.reload()

    def back(self, previous_screen: Optional[ScreenBase] = None):
        self.maze_manager.save_mazes()
        self.manager.back(previous_screen)

    def reload(self):
        self.maze_manager.load_mazes()
        self.selected_maze = None
        self.add_buttons()
