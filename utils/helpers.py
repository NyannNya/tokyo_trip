# helpers.py
import os

def check_folder_exists(folder_path):
    return os.path.isdir(folder_path)
