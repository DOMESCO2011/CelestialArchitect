# --- engine/renderer.py ---

import pygame
from config import settings

def draw_all(screen, state, sky_data, modules_data):
    screen.fill(settings.BG_COLOR)

    # Égbolt
    for obj in sky_data:
        x = int((obj["ra"] % 360) / 360 * settings.SCREEN_SIZE[0])
        y = int((90 - obj["dec"]) / 180 * settings.SCREEN_SIZE[1])
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)

    # Műhold modulok kirajzolása
    for placed in state.placed_modules:
        pygame.draw.rect(screen, (200, 200, 255), (*placed["pos"], 10, 10))