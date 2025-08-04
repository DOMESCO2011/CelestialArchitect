# --- utils/loader.py ---

import json
import os
import pygame

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_module_images(modules_data, image_folder="assets/modules"):
    images = {}
    for module in modules_data:
        name = module["name"]
        filename = module.get("filename", f"{name.lower()}.png")
        path = os.path.join(image_folder, filename)
        if os.path.exists(path):
            images[name] = pygame.image.load(path).convert_alpha()
        else:
            print(f"[WARN] Hiányzó kép: {path}")
    return images
