# Name: 

from Athlete import *
from abc import ABC, abstractmethod
   
class Dancer(Athlete, ABC):
    def dance(self):
         for k in range(1, 10):
            self.myDanceStep()

    @abstractmethod
    def myDanceStep(self):
        pass
            ## this method is abstract
            ## myDanceStep should be implemented in subclasses
            ## self.myDanceStep()

# --------------- Define new classes here ---------------------
    
