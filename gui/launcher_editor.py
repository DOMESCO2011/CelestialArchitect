import pygame

PANEL_WIDTH = 200  # bal oldali panel szélessége
MODULE_SIZE = 48   # minden komponens ikonmérete (px)

def draw(state, screen, modules_data):
    # Háttér
    pygame.draw.rect(screen, (30, 30, 60), screen.get_rect())  # sötét háttér

    # Bal oldali modul panel
    draw_module_panel(screen, modules_data, state)

    # Építési terület (középső rész)
    draw_build_area(screen, state)

    # Épp húzott modul megjelenítése
    draw_dragging(screen, state)

def draw_module_panel(screen, modules_data, state):
    pygame.draw.rect(screen, (20, 20, 40), (0, 0, PANEL_WIDTH, screen.get_height()))
    font = pygame.font.SysFont(None, 18)

    for i, module in enumerate(modules_data):
        x = 10
        y = 10 + i * (MODULE_SIZE + 10)
        rect = pygame.Rect(x, y, MODULE_SIZE, MODULE_SIZE)
        pygame.draw.rect(screen, (80, 80, 120), rect)

        label = font.render(module["name"], True, (200, 200, 255))
        screen.blit(label, (x + MODULE_SIZE + 5, y + 10))

        # Később: mentés a state-be kattintás észleléshez

def draw_build_area(screen, state):
    pygame.draw.rect(screen, (40, 40, 70), (PANEL_WIDTH, 0, screen.get_width() - PANEL_WIDTH, screen.get_height()))

    # Helyezett modulok kirajzolása (ha vannak)
    for placed in state.placed_modules:
        screen.blit(placed["surface"], placed["pos"])

def draw_dragging(screen, state):
    if state.dragging_module:
        pos = pygame.mouse.get_pos()
        screen.blit(state.dragging_module["surface"], (pos[0] - MODULE_SIZE // 2, pos[1] - MODULE_SIZE // 2))
