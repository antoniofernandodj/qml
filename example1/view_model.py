from PySide6.QtCore import (
    Property,
    QObject,
    Signal,
    Slot,
)

from example1.reactive import ref


class CounterViewModel(QObject):
    counter, counterChanged, _counter_name = ref(int, "counter")
    message, messageChanged, _message_name = ref(str, "message")

    def __init__(self):
        super().__init__()

        self._counter = 0
        self._message = "Clique no botão!"

        # Conecta reatividade derivada
        self.counterChanged.connect(self._update_message)

    @Slot()
    def increment(self):
        self.counter += 1

    @Slot()
    def decrement(self):
        self.counter -= 1

    @Slot()
    def reset(self):
        self.counter = 0

    def _update_message(self, value: int):
        if value == 0:
            self.message = "Comece a contar!"
        elif value < 5:
            self.message = f"Você está em {value}"
        elif value < 10:
            self.message = "Está aumentando!"
        else:
            self.message = "Uau! Mais de 10!"
