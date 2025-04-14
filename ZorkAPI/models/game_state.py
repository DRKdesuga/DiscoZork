import json

class GameState:
    def __init__(self):
        self.variables = {}
        self.history = []

    def update(self, variable_name: str, value):
        self.variables[variable_name] = value

    def save_session(self, file_path: str = "game_state.json"):
    
        data = {"variables": self.variables, "history": self.history}
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving session: {e}")

    def load_session(self, file_path: str = "game_state.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.variables = data.get("variables", {})
                self.history = data.get("history", [])
        except Exception as e:
            print(f"Error loading session: {e}")

    def __repr__(self):
        return f"<GameState(variables={self.variables}, history={self.history})>"
