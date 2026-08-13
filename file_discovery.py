import os
from config import SHARED_FOLDER, logger

def discover_user_files(shared_folder=SHARED_FOLDER):
    user_files = {}
    for entry in os.scandir(shared_folder):
        username = entry.name
        sdf_files = [
            f.path for f in os.scandir(entry.path)
            if f.is_file() and f.name.lower().endswith(".sdf")
        ]
        if sdf_files:
            user_files[username] = sdf_files
        else:
            logger.info(f"No SDF files found for user: '{username}'")
    return user_files