from PySide6.QtCore import Property, Signal




def ref(_type: type, name: str):
    """
    Cria (Property, Signal) reativos compatíveis com PySide6.
    Nome da propriedade é explícito (exigência do Qt).
    """
    signal = Signal(_type)
    private_name = f"_{name}"

    def getter(self):
        return getattr(self, private_name)

    def setter(self, value):
        if getattr(self, private_name, None) == value:
            return

        setattr(self, private_name, value)
        getattr(self, f"{name}Changed").emit(value)

    prop = Property(_type, getter, setter, notify=signal)

    return prop, signal