from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def area(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato**2

class Cerchio(Forma):

    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return self.raggio**2 * 3.14