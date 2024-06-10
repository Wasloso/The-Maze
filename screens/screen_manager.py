from screens import ScreenBase


class ScreenManager:
    current_screen: ScreenBase = None

    def update(self, events, keys):
        if self.current_screen:
            self.current_screen.update(events, keys)

    def draw(self, screen):
        if self.current_screen:
            self.current_screen.draw(screen)

    # def handle_events(self):