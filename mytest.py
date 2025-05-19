import pytest


class bazowa:
    def __init__(self):
        self.aaa = 5


class nowa(bazowa):
    def __init__(self):
        super().__init__()

    def showAAA(self):
        return self.aaa
    

o = nowa()
print(o.aaa)

