from typing import Union

from PySide6.QtCore import (
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
    Signal,
    Slot,
)

from example1.model.task import Task
from example1.repository.task_repository import TaskRepository


class TaskListModel(QAbstractListModel):
    TextRole = Qt.ItemDataRole.UserRole + 1
    CompletedRole = Qt.ItemDataRole.UserRole + 2
    
    # Signal para indicar operações assíncronas
    loadingChanged = Signal(bool)
    errorOccurred = Signal(str)
    
    def __init__(self, repository: TaskRepository):
        super().__init__()
        self.repository = repository
        self.tasks = []
        self.loading = False
        self.load_tasks()
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.tasks)

    def data(
        self,
        index: Union[QModelIndex, QPersistentModelIndex],
        role = Qt.ItemDataRole.DisplayRole
    ):
        if not index.isValid() or index.row() >= len(self.tasks):
            return None

        task = self.tasks[index.row()]
        if role == self.TextRole:
            return task.text
        elif role == self.CompletedRole:
            return task.completed
        return None

    def roleNames(self):
        return {
            self.TextRole: b"text",
            self.CompletedRole: b"completed"
        }
    
    @Slot()
    def load_tasks(self):
        """Carrega tarefas do repositório"""
        self.set_loading(True)
        
        # Carrega do repositório
        tasks = self.repository.get_all()
        
        # Atualiza o model
        self.beginResetModel()
        self.tasks = tasks
        self.endResetModel()
        
        self.set_loading(False)
    
    @Slot(str)
    def addTask(self, text: str):
        """Adiciona tarefa e persiste"""
        if not text.strip():
            return
        
        new_task = Task(text)
        
        # Persiste no repositório
        if self.repository.add(new_task):
            # Atualiza UI reativamente
            self.beginInsertRows(
                QModelIndex(), len(self.tasks), len(self.tasks)
            )
            self.tasks.append(new_task)
            self.endInsertRows()
        else:
            self.errorOccurred.emit("Erro ao adicionar tarefa")
    
    @Slot(int)
    def removeTask(self, index: int):
        """Remove tarefa e persiste"""
        if not (0 <= index < len(self.tasks)):
            return

        # Persiste no repositório
        if self.repository.remove(index):
            # Atualiza UI reativamente
            self.beginRemoveRows(QModelIndex(), index, index)
            del self.tasks[index]
            self.endRemoveRows()
        else:
            self.errorOccurred.emit("Erro ao remover tarefa")
    
    @Slot(int)
    def toggleTask(self, index: int):
        """Alterna status e persiste"""
        if not (0 <= index < len(self.tasks)):
            return
        
        # Atualiza em memória
        self.tasks[index].completed = not self.tasks[index].completed
        
        # Persiste no repositório
        if self.repository.update(index, self.tasks[index]):
            # Notifica UI da mudança
            model_index = self.index(index, 0)
            self.dataChanged.emit(
                model_index, model_index, [self.CompletedRole]
            )
        else:
            # Reverte em caso de erro
            self.tasks[index].completed = not self.tasks[index].completed
            self.errorOccurred.emit("Erro ao atualizar tarefa")
    
    def set_loading(self, loading: bool):
        """Atualiza estado de loading"""
        if self.loading != loading:
            self.loading = loading
            self.loadingChanged.emit(loading)
