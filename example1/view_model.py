from PySide6.QtCore import QObject, Slot
from example1.reactive import use_ref


class CounterViewModel(QObject):
    counter, counterChanged = use_ref(int, "counter")
    message, messageChanged = use_ref(str, "message")

    def __init__(self, message: str):
        super().__init__()
        self.counter = 0
        self.message = message
        self.counterChanged.connect(self.update_message)

    @Slot()
    def increment(self):
        self.counter += 1

    @Slot()
    def decrement(self):
        self.counter -= 1

    @Slot()
    def reset(self):
        self.counter = 0

    def update_message(self, value: int):
        if value == 0:
            self.message = "Comece a contar!"
        elif value < 5:
            self.message = f"Você está em {value}"
        elif value < 10:
            self.message = "Está aumentando!"
        else:
            self.message = "Uau! Mais de 10!"
