from PySide6.QtCore import Property, Signal


def use_ref(_type: type, name: str):
    signal = Signal(_type)

    def getter(self):
        return getattr(self, f"_{name}")

    def setter(self, value):
        if getattr(self, f"_{name}", None) == value:
            return

        setattr(self, f"_{name}", value)
        getattr(self, f"{name}Changed").emit(value)

    prop = Property(_type, getter, setter, notify=signal)
    return prop, signal
