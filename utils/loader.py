import os
import json
import pygame

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_module_images(modules_data):
    images = {}
    base_path = os.path.join("assets", "sprites", "modules")

    for module in modules_data:
        icon_filename = module.get("icon")
        if icon_filename:
            image_path = os.path.join(base_path, icon_filename)
            if os.path.exists(image_path):
                images[module["name"]] = pygame.image.load(image_path).convert_alpha()
            else:
                print(f"[HIBA] Hiányzó kép: {image_path}")
    return images
