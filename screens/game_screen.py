from pygame.surface import Surface

from maze.maze import Maze
from maze.objective import Objective
from maze.player import Player
from screens.screen_base import *
from ui_components.button import Button
from assets.assets_loader import AssetsLoader


class GameScreen(ScreenBase):
    def __init__(
        self,
        previous_screen: Optional[ScreenBase],
        manager,
        maze: Maze,
        ai: bool = False,
    ) -> None:
        super().__init__(previous_screen, manager, GAME)
        self.maze = maze
        self.ai = ai

        # player_img = pygame.image.load("assets/player.png")
        playerImg = AssetsLoader.get_player("idle" if not ai else "idle_ai")
        self.player = Player(
            self.maze.player_start, 2, size=self.maze.cell_size // 3, image=playerImg
        )
        self.objective = Objective(
            self.maze.objective_position, size=self.maze.cell_size // 2
        )
        self.back_button = Button.go_back_button(
            position=(25, 25),
            desiredSize=(50, 50),
            callback=lambda: self.manager.back(previous_screen),
            # TODO: change to play screen when implemented
        )
        self.cells = [cell for row in self.maze.grid for cell in row]
        self.collidable_cells = [cell.rect for cell in self.cells if cell.collidable]
        self.wallImage = AssetsLoader.get_cell("wall")
        self.floorImage = AssetsLoader.get_cell("floor")

    def draw(self, surface: Surface) -> None:
        # super().draw(screen) - renderowanie tla bardzo obniza fps
        for cell in self.cells:
            if cell.collidable:
                surface.blit(self.wallImage, cell.rect)
            else:
                surface.blit(self.floorImage, cell.rect)
        self.player.draw(surface)
        self.objective.draw(surface)
        self.back_button.draw(surface)

    def update(self, events: list, keys) -> None:
        for event in events:
            self.back_button.update(event)
        self.handle_buttons_click(keys)
        if self.objective.check_collision(self.player.rect):
            # TODO: Implement win screen
            pass

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
