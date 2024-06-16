import pygame
from pygame.surface import Surface
from pygame.event import Event
from .button import Button
from .ui_component import UIComponent
from assets.assets_loader import AssetsLoader
from data import SettingsManager


class VolumeController(UIComponent):
    def __init__(
        self,
        position: tuple[int, int],
        desired_size: tuple[int, int],
        settings_manager: SettingsManager,
    ) -> None:
        image = Surface(desired_size, pygame.SRCALPHA)
        image.fill((0, 0, 0, 0))
        super().__init__(position, desired_size, image)
        self.settings_manager: SettingsManager = settings_manager

        self.volume_text = UIComponent(
            image=AssetsLoader.get_text("Volume"), desired_size=(200, 50)
        )
        self.volume_up_button = Button(
            image=AssetsLoader.get_button("volume_up_button"),
            alt_image=AssetsLoader.get_button("volume_up_button", hovered=True),
            desired_size=(30, 30),
            callback=lambda: self.settings_manager.change_volume(True),
        )
        self.volume_down_button = Button(
            image=AssetsLoader.get_button("volume_down_button"),
            alt_image=AssetsLoader.get_button("volume_down_button", hovered=True),
            desired_size=(30, 30),
            callback=lambda: self.settings_manager.change_volume(False),
        )
        self.active_cell_image = AssetsLoader.get_volume_cell(True)
        self.inactive_cell_image = AssetsLoader.get_volume_cell(False)
        self.volume_cells = [
            UIComponent(desired_size=(30, 40), image=self.inactive_cell_image)
            for _ in range(10)
        ]

        self.unmuted_image = AssetsLoader.get_button("unmuted_button")
        self.unmuted_alt = AssetsLoader.get_button("unmuted_button", hovered=True)
        self.muted_image = AssetsLoader.get_button("muted_button")
        self.muted_alt = AssetsLoader.get_button("muted_button", hovered=True)
        self.mute_button = Button(
            image=self.muted_image if settings_manager.mute else self.unmuted_image,
            alt_image=self.muted_alt if settings_manager.mute else self.unmuted_alt,
            desired_size=(100, 100),
            callback=lambda: self.toggle_mute(),
        )

    def draw(self, screen: Surface, position: tuple[int, int] = None) -> None:
        super().draw(screen, position)
        # FIXME: adjust positions
        self.volume_text.draw(
            screen,
            position=(
                self.rect.x + self.rect.width // 2 - self.volume_text.rect.width // 2,
                self.rect.y - self.volume_text.rect.height - 20,
            ),
        )
        self.volume_down_button.draw(
            screen,
            (self.rect.x - 50, self.rect.y + 5),
        )
        self.volume_up_button.draw(
            screen,
            (
                self.rect.x + self.rect.width + 30 - self.volume_down_button.rect.width,
                self.rect.y + 5,
            ),
        )
        for i, cell in enumerate(self.volume_cells):
            if (
                i < self.settings_manager.volume // 10
                and not self.settings_manager.mute
            ):
                cell.change_image(self.active_cell_image)
            else:
                cell.change_image(self.inactive_cell_image)
            cell.draw(
                screen,
                (self.rect.x + 50 * i, self.rect.y),
            )

        self.mute_button.draw(
            screen,
            position=(
                screen.get_rect().width // 2 - self.mute_button.rect.width // 2,
                screen.get_rect().height // 2
                - self.rect.height // 2
                + self.rect.height,
            ),
        )

    def update(self, event: Event) -> None:
        self.volume_up_button.update(event)
        self.volume_down_button.update(event)
        self.mute_button.update(event)

    def toggle_mute(self):
        mute = self.settings_manager.toggle_mute()
        self.mute_button.change_image(
            self.muted_image if mute else self.unmuted_image,
            self.muted_alt if mute else self.unmuted_alt,
        )
        self.volume_down_button.callback = lambda: (
            self.settings_manager.change_volume(False) if not mute else None
        )
        self.volume_up_button.callback = lambda: (
            self.settings_manager.change_volume(True) if not mute else None
        )
