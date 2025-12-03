import os

def ensure_dirs(dir_list):
    """
    Ensures that all directories in dir_list exist.
    Creates them if they are missing.
    """
    for d in dir_list:
        os.makedirs(d, exist_ok=True)
