from pathlib import Path
import sys

from example1.model.task_list import TaskListModel
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from example1.repository.task_repository import TaskRepository

from example1.view_model import CounterViewModel



def set_context(engine, context):
    rc = engine.rootContext()
    for key, item in context.items():
        rc.setContextProperty(key, item)


def main():
    app = QGuiApplication(sys.argv)

    # Cria ViewModels e Models
    counter_vm = CounterViewModel(message="Clique no botão!")
    task_model = TaskListModel(
        repository=TaskRepository(Path(__file__).parent / "tasks.json")
    )

    # Configura QML Engine
    engine = QQmlApplicationEngine()
    set_context(engine, {
        "counterVM": counter_vm,
        "taskListModel": task_model
    })

    # Carrega QML
    with open(Path(__file__).parent / 'interface.qml') as f:
        engine.loadData(f.read().encode())
    
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
