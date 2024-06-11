from .screen_base import *
from pygame.surface import Surface
from pygame import Surface
from ui_components.button import Button


class MazeSelectionScreen(ScreenBase):
    def __init__(self, previous_screen: Optional[ScreenBase], manager) -> None:
        super().__init__(previous_screen, manager, screen_name=MAZE_SELECTION)
        self.back_button = Button.go_back_button(
            position=(50, 50), callback=lambda: self.manager.back(previous_screen)
        )

    def draw(self, surface: Surface) -> None:
        super().draw(surface)
        self.back_button.draw(surface)

    def update(self, events, keys) -> None:
        super().update(events, keys)
        for event in events:
            self.back_button.update(event)
