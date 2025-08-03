# --- gui/hud.py ---

import pygame
from config import settings

def draw(state, screen):
    font = pygame.font.SysFont(settings.FONT_NAME, settings.FONT_SIZE)
    text = font.render(f"Mouse: {state.mouse_pos} | Weather: {state.weather_state}", True, (255, 255, 255))
    screen.blit(text, (10, 10))