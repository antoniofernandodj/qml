from PySide6.QtCore import Property, Signal


def ref(_type, name: str):
    signal = Signal(_type)
    private_name = f"_{name}"

    def getter(self):
        return getattr(self, private_name)

    def setter(self, value):
        if getattr(self, private_name) != value:
            setattr(self, private_name, value)
            getattr(self, f"{name}Changed").emit(value)

    prop = Property(_type, getter, setter, notify=signal)
    return prop, signal, private_name