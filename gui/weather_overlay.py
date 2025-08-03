# --- gui/weather_overlay.py ---

import pygame

def draw(screen, state):
    if state.weather_state == "cloudy":
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((100, 100, 100, 50))
        screen.blit(overlay, (0, 0))