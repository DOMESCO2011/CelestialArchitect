# --- engine/renderer.py ---

import pygame
from config import settings

PANEL_WIDTH = 350
MODULE_SIZE = 32

def draw_all(screen, state, sky_data, modules_data, module_images):
    screen.fill(settings.BG_COLOR)

    # Égbolt megrajzolása
    draw_sky(screen, sky_data)

    # Bal oldali modul panel
    draw_module_panel(screen, modules_data, state, module_images)

    # Műhold modulok kirajzolása a térképen
    draw_placed_modules(screen, state, module_images)

    # Húzás közben modul megjelenítés
    draw_dragging_module(screen, state)

def draw_sky(screen, sky_data):
    for obj in sky_data:
        x = int((obj["ra"] % 360) / 360 * settings.SCREEN_SIZE[0])
        y = int((90 - obj["dec"]) / 180 * settings.SCREEN_SIZE[1])
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)

def draw_module_panel(screen, modules_data, state, module_images):
    pygame.draw.rect(screen, (20, 20, 40), (0, 0, PANEL_WIDTH, screen.get_height()))
    font = pygame.font.SysFont(settings.FONT_NAME, settings.FONT_SIZE)

    for i, module in enumerate(modules_data):
        x = 10
        y = 10 + i * (MODULE_SIZE + 10)

        # Háttér a modulnak
        rect = pygame.Rect(x, y, MODULE_SIZE, MODULE_SIZE)
        pygame.draw.rect(screen, (80, 80, 120), rect)

        # Modul képe
        image = module_images.get(module["name"])
        if image:
            screen.blit(image, (x, y))

        # Felirat
        label = font.render(module["name"], True, (200, 200, 255))
        screen.blit(label, (x + MODULE_SIZE + 5, y + 6))

def draw_placed_modules(screen, state, module_images):
    for placed in state.placed_modules:
        image = module_images.get(placed["name"])
        if image:
            screen.blit(image, placed["pos"])

def draw_dragging_module(screen, state):
    if state.dragging_module:
        image = state.dragging_module.get("image")
        if image:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(image, (mouse_x - MODULE_SIZE // 2, mouse_y - MODULE_SIZE // 2))
