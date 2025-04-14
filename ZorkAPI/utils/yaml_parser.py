import yaml
from ZorkAPI.models.story_choice import StoryChoice
from ZorkAPI.models.story_node import StoryNode

def load_yaml(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def parse_story(yaml_data: dict) -> (str, str, list):
    title = yaml_data.get("title", "No Title")
    scripts_path = yaml_data.get("scripts-path", "")
    story_nodes = []
    for node_data in yaml_data.get("story", []):
        name = node_data.get("name")
        script = node_data.get("script")
        choices = [
            StoryChoice(choice.get("text"), choice.get("target"))
            for choice in node_data.get("choices", [])
        ]
        story_nodes.append(StoryNode(name, script, choices))
    return title, scripts_path, story_nodes
