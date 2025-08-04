import os

def print_tree(start_path, prefix=""):
    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        print(prefix + "└── <Nincs jogosultság>")
        return

    entries = [e for e in entries if not e.startswith(".")]  # Rejtett fájlok kihagyása
    for i, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        connector = "├── " if i < len(entries) - 1 else "└── "
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = "│   " if i < len(entries) - 1 else "    "
            print_tree(path, prefix + extension)

if __name__ == "__main__":
    path = input("Add meg a könyvtár elérési útját: ").strip('"').strip("'")
    if not os.path.isdir(path):
        print("Hiba: A megadott útvonal nem létező könyvtár.")
    else:
        print(os.path.basename(os.path.abspath(path)) + "/")
        print_tree(path)
