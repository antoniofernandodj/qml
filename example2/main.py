"""
Exemplo de Componentes Reutilizáveis em QML
Mostra 2 formas: arquivos separados e componentes inline
"""

import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from example2.view_model import CounterViewModel



# example2.main.py::main()
def main():
    app = QGuiApplication(sys.argv)

    counter_vm = CounterViewModel()
    engine = QQmlApplicationEngine()
    engine.addImportPath(Path(__file__).parent)
    rc = engine.rootContext()
    rc.setContextProperty("counterVM", counter_vm)

    engine.load(Path(__file__).parent / 'main.qml')
    
    if not engine.rootObjects():
        print("❌ Erro ao carregar QML")
        sys.exit(-1)
    
    sys.exit(app.exec())
