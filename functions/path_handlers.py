from pathlib import Path


def get_path() -> Path:
    current_path = Path.cwd()

    return current_path