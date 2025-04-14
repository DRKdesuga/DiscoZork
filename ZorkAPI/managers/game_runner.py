# ZorkAPI/managers/game_runner.py

import os
from ZorkAPI.managers.story_manager import StoryManager
from ZorkAPI.models.game_state import GameState

class GameRunner:
    def __init__(self, yaml_file: str):
        self.story_manager = StoryManager(yaml_file)
        self.game_state = GameState()
        # Set current node to the first node in the story (if available)
        self.current_node = None
        if self.story_manager.nodes:
            first_node_key = list(self.story_manager.nodes.keys())[0]
            self.current_node = self.story_manager.get_node(first_node_key)

    def load_script(self, node) -> str:
        script_file = os.path.join(self.story_manager.scripts_path, node.script)
        try:
            with open(script_file, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Error loading script: {e}"

    def process_choice(self, choice_index: int):
        choices = self.current_node.choices
        if 0 <= choice_index < len(choices):
            target_name = choices[choice_index].target
            self.game_state.history.append(self.current_node.name)
            self.current_node = self.story_manager.get_node(target_name)
        else:
            print("Invalid choice. Please try again.")

    def get_pretty_output(self):
        """Return a nicely formatted output for the current node."""
        node = self.current_node
        script = self.load_script(node)
        output = f"**{node.name.capitalize()}**\n"
        output += f"```\n{script}\n```\n"  # use code block for the script
        if node.choices:
            output += "Choices:\n"
            for i, choice in enumerate(node.choices):
                output += f"{i+1}. {choice.text}\n"
        else:
            output += "**The End.**"
        return output

    def run(self):
        while self.current_node:
            print("\n" + "-" * 40)
            print(self.get_pretty_output())
            print("-" * 40)
            if not self.current_node.choices:
                print("The End.")
                break
            user_input = input("Your choice: ")
            try:
                index = int(user_input.strip()) - 1
                self.process_choice(index)
            except ValueError:
                print("Please enter a valid number.")
