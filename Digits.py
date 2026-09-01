# Fill in the segment methods and write each subclass
# of Digit define the abstract method Display()

from Athlete import *
from abc import ABC, abstractmethod

class Digit(ABC, Athlete):
    def __init__(self, w, x=1, y=1, d=east, b=infinity):
        Athlete.__init__(self, w, x, y, d, b)
        
    @abstractmethod
    def display(self):
      pass
        ## this method is abstract
        ## display() should be implemented in subclasses
     

    def threeNoTurn(self, on):
        for x in range(3):
            self.move()
            if(on):
               self.putBeeper()
        self.move() 
     
    def threeAndTurn(self, on):
        self.threeNoTurn(on) 
        self.turnRight()
    
    def segment1_On(self):
        self.threeAndTurn(True)

    def segment1_Off(self):
        self.threeAndTurn(False)

# define more segments, both on and off

          
          
#-------------------- SUB CLASSES --------------------------------  
      
class Zero(Digit):     
    def display(self):
        self.segment1_On()
        self.segment2_On()
        self.segment3_On()
        self.segment4_On()
        self.segment5_On()
        self.segment6_On()
        self.segment7_Off()
        
# define all the Digit subclasses and their display method