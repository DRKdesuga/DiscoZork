
import os

def get_story_folders(stories_root: str) -> list:
    try:
        return [d for d in os.listdir(stories_root) if os.path.isdir(os.path.join(stories_root, d))]
    except Exception:
        return []
