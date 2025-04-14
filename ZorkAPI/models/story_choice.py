class StoryChoice:

    def __init__(self, text: str, target: str):
        self.text = text
        self.target = target

    def __repr__(self):
        return f"<StoryChoice text={self.text} target={self.target}>"
