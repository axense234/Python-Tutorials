# you private things by adding an _ before them
class _Private:
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.private = _Private(name)

    def _display(self):
        print("Hello")

    def display(self):
        print("Hi")