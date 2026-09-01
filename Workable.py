#Name: Grover

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def doYourThing(self):
        pass

    @abstractmethod
    def turnToTheNorth(self):
        pass