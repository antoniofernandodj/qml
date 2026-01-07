import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from model.task_list import TaskListModel
from repository.task_repository import TaskRepository
from view_model import CounterViewModel

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    # Cria ViewModels e Models
    counter_vm = CounterViewModel()
    task_model = TaskListModel(repository=TaskRepository("tasks.json"))
    
    # Configura QML Engine
    engine = QQmlApplicationEngine()
    
    # Expõe objetos Python para QML (Context Properties)
    rc = engine.rootContext()
    rc.setContextProperty("counterVM", counter_vm)
    rc.setContextProperty("taskListModel", task_model)
    
    # Carrega QML
    with open('interface.qml') as f:
        engine.loadData(f.read().encode())
    
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())