from .screen_base import *
from typing import Optional
from pygame.surface import Surface
from pygame import Surface
from pygame.font import Font
from ui_components.button import Button
from data import MazeManager
from ui_components.ui_component import UIComponent


class MazeSelectionScreen(ScreenBase):
    def __init__(self, previous_screen: Optional[ScreenBase], manager) -> None:
        super().__init__(previous_screen, manager, screen_name=MAZE_SELECTION)

        self.selection_buttons: list[Button] = []
        self.maze_manager = MazeManager()
        self.maze_manager.load_mazes()
        self.selected_maze = None
        self.scroll_offset = 0
        self.scroll_max = 0

        self.add_selection_buttons()

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
        self.select_maze_idx = None

    def draw(self, surface: Surface) -> None:
        super().draw(surface)
        self.back_button.draw(surface)
        for i, button in enumerate(self.selection_buttons):
            button.draw(
                surface,
                (
                    50 + (i * (button.rect.width + 50)) - self.scroll_offset,
                    surface.get_height() // 2 - button.rect.height // 2,
                ),
            )
            if self.select_maze_idx is not None and i == self.select_maze_idx:
                image = button.displayImage.copy()
                image.fill((255, 255, 0))
                image.set_alpha(128)
                surface.blit(
                    image,
                    (button.rect,),
                )

        for i, button in enumerate(self.action_buttons):
            button.draw(
                surface,
                (
                    surface.get_width() // 2 - 50 * len(self.action_buttons) + 125 * i,
                    surface.get_height() - 150,
                ),
            )

    def add_selection_buttons(self):
        self.selection_buttons.clear()
        font = Font(None, 100)
        text_color = (0, 0, 0)
        alt_text_color = (0, 150, 0)
        size = (400, 300)
        background = pygame.transform.scale(
            AssetsLoader.get_button("selection_button"), size
        )

        for idx, maze in enumerate(self.maze_manager.mazes):
            image = UIComponent.add_text_to_surface(
                text=maze.name,
                font=font,
                text_color=text_color,
                surface=background.copy(),
            )
            altImage = UIComponent.add_text_to_surface(
                text=maze.name,
                font=font,
                text_color=alt_text_color,
                surface=background.copy(),
            )
            self.selection_buttons.append(
                Button(
                    image=image,
                    alt_image=altImage,
                    desired_size=size,
                    callback=lambda m=maze, i=idx: self.select_maze(maze=m, idx=i),
                )
            )
        total_width = (
            len(self.selection_buttons) * (self.selection_buttons[0].rect.width + 75)
            if len(self.selection_buttons) != 0
            else 0
        )
        self.scroll_max = max(0, total_width - 1280)
        self.scroll_offset = max(self.scroll_offset, 0)

    def update(self, events, keys) -> None:
        super().update(events, keys)
        for event in events:
            self.back_button.update(event)
            for button in [*self.selection_buttons, *self.action_buttons]:
                button.update(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.scroll_offset = max(self.scroll_offset - 10, 0)
                elif event.button == 5:
                    self.scroll_offset = min(self.scroll_offset + 10, self.scroll_max)

    def select_maze(self, maze, idx):
        self.selected_maze = maze
        self.select_maze_idx = idx

    def delete_maze(self, maze):
        if (
            self.select_maze_idx
            and self.maze_manager.mazes[self.select_maze_idx] == maze
        ):
            self.select_maze_idx = None
        self.maze_manager.mazes.remove(maze)
        self.maze_manager.save_mazes()
        self.reload()

    def back(self, previous_screen: Optional[ScreenBase] = None):
        self.maze_manager.save_mazes()
        self.manager.back(previous_screen)

    def reload(self):
        self.maze_manager.load_mazes()
        self.selected_maze = None
        self.add_selection_buttons()
