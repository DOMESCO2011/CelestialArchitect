# --- engine/gamestate.py ---

class GameState:
    def __init__(self):
        self.running = True
        self.mouse_pos = (0, 0)
        self.selected_module = None
        self.placed_modules = []
        self.weather_state = "clear"

    def update(self):
        pass  # Ide jöhetnek az időalapú változások, animációk