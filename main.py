# main.py

import pygame
import os
from config import settings
from engine import gamestate, renderer, input, sky_logic
from gui import hud, launcher_editor, weather_overlay
from utils import loader
from assets import *

def main():
    pygame.init()
    flags = pygame.FULLSCREEN if settings.FULLSCREEN else 0
    screen = pygame.display.set_mode(settings.SCREEN_SIZE, flags)
    pygame.display.set_caption("Celestial Architect")
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "game", "icon.png")))
    
    clock = pygame.time.Clock()
    state = gamestate.GameState()

    # Betöltések
    sky_data = loader.load_json("data/sky_map.json")
    modules_data = loader.load_json("data/satellites.json")

    # Fő ciklus
    running = True
    while running:
        for event in pygame.event.get():
            input.handle_event(event, state)

        sky_logic.update(state)
        state.update()
        
        renderer.draw_all(screen, state, sky_data, modules_data)
        hud.draw(state, screen)
        weather_overlay.draw(screen, state)

        pygame.display.flip()
        clock.tick(settings.FPS)

if __name__ == "__main__":
    main()
