# --- engine/input.py ---

import pygame

def handle_event(event, state):
    if event.type == pygame.QUIT:
        state.running = False
    elif event.type == pygame.MOUSEMOTION:
        state.mouse_pos = event.pos
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if state.selected_module:
                state.placed_modules.append({
                    "type": state.selected_module,
                    "pos": state.mouse_pos
                })
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            state.selected_module = None