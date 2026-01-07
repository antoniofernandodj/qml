# repository/task_repository.py
"""
Repository pattern - responsável apenas por persistência de dados
Pode ser JSON, SQLite, API REST, etc.
"""
import json
from pathlib import Path
from typing import List, Optional
from model.task import Task


class TaskRepository:
    """Repository para persistência de tarefas em JSON"""
    
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = Path(file_path)
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not self.file_path.exists():
            self.file_path.write_text("[]")
    
    def get_all(self) -> List[Task]:
        """Carrega todas as tarefas do JSON"""
        try:
            data = json.loads(self.file_path.read_text())
            return [Task(item["text"], item.get("completed", False)) 
                    for item in data]
        except (json.JSONDecodeError, KeyError):
            return []
    
    def save_all(self, tasks: List[Task]) -> bool:
        """Salva todas as tarefas no JSON"""
        try:
            data = [{"text": task.text, "completed": task.completed} 
                    for task in tasks]
            self.file_path.write_text(json.dumps(data, indent=2))
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False
    
    def add(self, task: Task) -> bool:
        """Adiciona uma tarefa"""
        tasks = self.get_all()
        tasks.append(task)
        return self.save_all(tasks)
    
    def remove(self, index: int) -> bool:
        """Remove uma tarefa por índice"""
        tasks = self.get_all()
        if 0 <= index < len(tasks):
            tasks.pop(index)
            return self.save_all(tasks)
        return False
    
    def update(self, index: int, task: Task) -> bool:
        """Atualiza uma tarefa"""
        tasks = self.get_all()
        if 0 <= index < len(tasks):
            tasks[index] = task
            return self.save_all(tasks)
        return False
