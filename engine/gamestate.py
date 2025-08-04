# --- engine/gamestate.py ---

import random

class GameState:
    def __init__(self):
        self.money = 100_000_000  # kezdőtőke
        self.date = "2025-01-01"  # induló dátum
        self.selected_module = None  # épp épített elem
        self.selected_constellation = None
        self.sky_unlocked = {}  # konstellációk nyitása
        self.modules = []  # összerakott műholdak
        self.placed_modules = []
        self.mode = "view"  # view / build / launch stb.
        self.weather_state = "clear"  # vagy "cloudy", "stormy", stb.
        self.mode = "sim"  # vagy "menu", "editor" stb.
        self.mouse_pos = (0, 0)
        self.editor_button_rect = None
        self.dragging_module = None

    
    def update(self):
        pass

