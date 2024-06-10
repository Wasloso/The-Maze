import sys

from pygame.surface import Surface

sys.path.append("../")

from screens.screen_base import *
from maze.maze import Maze
from maze.player import Player
from maze.objective import Objective
from ui_components.button import Button
from assets.assets_loader import AssetsLoader


class GameScreen(ScreenBase):
    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        maze: Maze,
        ai: bool = False,
    ) -> None:
        super().__init__(title, width, height)
        self.maze = maze
        self.ai = ai
        # player_img = pygame.image.load("assets/player.png")
        self.player = Player(
            self.maze.player_start, 2, size=self.maze.cell_size // 3, image=None
        )
        self.objective = Objective(
            self.maze.objective_position, size=self.maze.cell_size // 3
        )
        self.back_button = Button.go_back_button(
            (0, 0),
            lambda: self.change_screen(MAIN_MENU),
            # TODO: change to play screen when implemented
        )
        self.cells = [cell for row in self.maze.grid for cell in row]
        self.collidable_cells = [cell.rect for cell in self.cells if cell.collidable]
        self.wallImage = AssetsLoader.get_cell("wall")
        self.floorImage = AssetsLoader.get_cell("floor")

    def draw(self, screen: Surface) -> None:
        # super().draw(screen) - renderowanie tla bardzo obniza fps
        for cell in self.cells:
            if cell.collidable:
                screen.blit(self.wallImage, cell.rect)
            else:
                screen.blit(self.floorImage, cell.rect)
        self.player.draw(screen)
        self.objective.draw(screen)
        self.back_button.draw(screen)

    def update(self, events: list, keys) -> None:
        for event in events:
            self.back_button.update(event)
        self.handle_buttons_click(keys)
        if self.objective.check_collision(self.player.rect):
            self.done = True
            self.next_screen = MAIN_MENU

    def handle_buttons_click(self, keys):
        multiplier = 2 if keys[pygame.K_LSHIFT] else 1
        if keys[pygame.K_UP]:
            self.move_player(pygame.K_UP, multiplier)
        if keys[pygame.K_DOWN]:
            self.move_player(pygame.K_DOWN, multiplier)
        if keys[pygame.K_LEFT]:
            self.move_player(pygame.K_LEFT, multiplier)
        if keys[pygame.K_RIGHT]:
            self.move_player(pygame.K_RIGHT, multiplier)

    def move_player(self, direction, multiplier=1):
        new_rect = self.player.try_move(direction, multiplier)
        if new_rect.collidelist(self.collidable_cells) == -1:
            self.player.rect = new_rect

    def makeCurrent(self) -> None:
        pass
