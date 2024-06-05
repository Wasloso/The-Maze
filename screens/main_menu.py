from .screen_base import ScreenBase
import pygame


class MainMenu(ScreenBase):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(title, width, height)

    def draw(self, screen: pygame.Surface) -> None:
        super(MainMenu, self).draw(screen)
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render("Press SPACE to start", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text, text_rect)

    def update(self, events: list, keys) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next = "game"
                    self.done = True
                    break

    def makeCurrent(self) -> None:
        pass
