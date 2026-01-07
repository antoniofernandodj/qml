# Model para Lista Reativa
class Task:
    def __init__(self, text: str, completed: bool = False):
        self.text = text
        self.completed = completed
