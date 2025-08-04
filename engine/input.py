# --- engine/input.py ---

import pygame

# input.py

def handle_event(event, state):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    if event.type == pygame.MOUSEMOTION:
        state.mouse_pos = event.pos

    if event.type == pygame.MOUSEBUTTONDOWN:
        if hasattr(state, 'editor_button_rect') and state.editor_button_rect.collidepoint(event.pos):
            state.mode = "editor"  # váltsunk editor módba
