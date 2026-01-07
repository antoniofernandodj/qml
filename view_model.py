from PySide6.QtCore import (
    Property,
    QObject,
    Signal,
    Slot,
)


# ViewModel Reativo - Propriedades observáveis
class CounterViewModel(QObject):
    # Signals para notificar mudanças
    counterChanged = Signal(int)
    messageChanged = Signal(str)
    
    def __init__(self):
        super().__init__()
        self._counter = 0
        self._message = "Clique no botão!"
    
    # Property reativa para counter
    @Property(int, notify=counterChanged)
    def counter(self):
        return self._counter
    
    @counter.setter  # type: ignore
    def counter(self, value):
        if self._counter != value:
            self._counter = value
            self.counterChanged.emit(value)
            # Atualiza mensagem automaticamente
            self._update_message()
    
    # Property reativa para message
    @Property(str, notify=messageChanged)
    def message(self):
        return self._message
    
    @message.setter  # type: ignore
    def message(self, value):
        if self._message != value:
            self._message = value
            self.messageChanged.emit(value)
    
    # Slot chamado do QML
    @Slot()
    def increment(self):
        self.counter = self._counter + 1
    
    @Slot()
    def decrement(self):
        self.counter = self._counter - 1
    
    @Slot()
    def reset(self):
        self.counter = 0
    
    def _update_message(self):
        if self._counter == 0:
            self.message = "Comece a contar!"
        elif self._counter < 5:
            self.message = f"Você está em {self._counter}"
        elif self._counter < 10:
            self.message = "Está aumentando!"
        else:
            self.message = "Uau! Mais de 10!"