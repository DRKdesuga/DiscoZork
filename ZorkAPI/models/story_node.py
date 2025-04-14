from typing import List
from ZorkAPI.models.story_choice import StoryChoice

class StoryNode:

    def __init__(self, name: str, script: str, choices: List[StoryChoice]):
        self.name = name
        self.script = script
        self.choices = choices

    def __repr__(self):
        return f"<StoryNode name={self.name} script={self.script} choices={len(self.choices)}>"
