from PySide6.QtCore import QObject, Slot
from example2.reactive import use_ref


class CounterViewModel(QObject):
    counter, counterChanged = use_ref(int, "counter")

    def __init__(self, parent=None):
        super().__init__(parent)
        self.counter = 0

    @Slot()
    def increment(self):
        self.counter += 1
