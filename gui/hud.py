# --- gui/hud.py ---

import pygame
from config import settings


def draw(state, screen):
    font = pygame.font.SysFont(settings.FONT_NAME, settings.FONT_SIZE)

    
    # "Editor" gomb kirajzolása
    button_rect = pygame.Rect(screen.get_width() - 120, 10, 100, 30)
    pygame.draw.rect(screen, (0, 100, 200), button_rect)
    btn_text = font.render("Editor", True, (255, 255, 255))
    screen.blit(btn_text, (button_rect.x + 10, button_rect.y + 5))
    state.editor_button_rect = button_rect  # eltároljuk klikkhez

