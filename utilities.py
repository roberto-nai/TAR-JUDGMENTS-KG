"""
utilities.py
"""

from pathlib import Path

def create_directory_with_gitkeep(directory: str) -> None:
    """Creates a directory and adds a .gitkeep file inside.

    Args:
        directory (str): The directory path to create.
    """
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
    gitkeep_path = dir_path / '.gitkeep'
    gitkeep_path.touch(exist_ok=True)
    print(f"Directory '{dir_path}' and .gitkeep file created")