# ZorkAPI/managers/story_manager.py

import os
from typing import Dict
from ZorkAPI.models.story_node import StoryNode
from ZorkAPI.utils.yaml_parser import load_yaml, parse_story

class StoryManager:
    def __init__(self, yaml_file: str):
        yaml_data = load_yaml(yaml_file)
        self.title, relative_scripts_path, story_nodes = parse_story(yaml_data)
        self.scripts_path = os.path.abspath(os.path.join(os.path.dirname(yaml_file), relative_scripts_path))
        self.nodes: Dict[str, StoryNode] = {node.name: node for node in story_nodes}

    def get_node(self, name: str) -> StoryNode:
        return self.nodes.get(name)
