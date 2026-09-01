from pyKarel import *
import random
from abc import ABC, abstractmethod

class Ghost(Robot):
    def __init__(self, w, x=1, y=1, d=north, b=0, picName = "pacBot", fileName="ghost5"):
        self.canBeEaten = False
        Robot.__init__(self,w, x, y, d, b, picName, fileName)
        self.delay = 2 
    
    def goBlue(self):
        self.setImages("pacBot", "ghost5")
        self.draw()

    def turnRight(self):
        for i in range(3):
            self.turnLeft()

    def turnAround(self):
        for i in range(2):
            self.turnLeft()
    
    def faceEast(self):
        while not self.facingEast():
            self.turnLeft()
    
    def faceWest(self):
        while not self.facingWest():
            self.turnLeft()
    
    def faceSouth(self):
        while not self.facingSouth():
            self.turnLeft()
    
    def faceNorth(self):
        while not self.facingNorth():
            self.turnLeft()

    def randMove(self):
        num = random.randint(0, 2)
        if( num == 0):
            self.turnLeft()
        elif num == 1:
            self.turnRight()
        else:
            self.turnAround()
        if self.frontIsClear():
            self.move()
        
    def makeMove(self, avenue, street):
        for i in range(self.delay):         #to slow ghost down
            self.turnAround()
        self.makeNextMove(avenue, street)
      
    @abstractmethod
    def makeNextMove(self, avenue, street):
      pass
        ## this method is abstract
        ## should be implemented in subclasses

##-------------------- SUB CLASSES -------------------------------- 
#red ghost
class RandomFollower(Ghost):
    def __init__(self, w, x=1, y=1, d=north, b=0):
        Ghost.__init__(self,w, x, y, d, b, "pacBot", "ghost1")
        self.delay = 2 

    def makeNextMove(self, avenue, street):
        self.randMove()
        if self.frontIsClear():
            self.move()
        
            

##-----------------------------------------------------------------
#pink ghost
class AvenueFollower(Ghost):
    def __init__(self, w, x=1, y=1, d=north, b=0):
        Ghost.__init__(self,w, x, y, d, b, "pacBot", "ghost2")
        self.delay = 2 

    def makeNextMove(self, avenue, street):
        if (self.x < avenue):
            self.faceEast()
            if(self.frontIsClear()):
                self.move() 
            else:
                self.randMove()
        elif (self.x > avenue):
            self.faceWest()
            if(self.frontIsClear()):
                self.move()
            else:
                self.randMove()
        else:
            self.randMove()
            

    def orginal(self, avenue, street):
        if(self.frontIsClear()):
            self.move()
        elif (self.leftIsClear() and self.rightIsClear()):
            if(self.facingNorth() and avenue < self.x):
                self.turnLeft()
                self.move()
            elif(self.facingNorth() and avenue > self.x):
                self.turnRight()
                self.move()
            else:
                if(self.facingSouth() and avenue > self.x):
                    self.turnLeft()
                    self.move()
                elif(self.facingSouth() and avenue < self.x):
                    self.turnRight()
                    self.move()
                else:
                    self.randMove()
        elif(self.leftIsClear()):
            if(self.facingNorth() and avenue > self.x):
                self.turnLeft()
                self.move()
            elif(self.facingSouth() and avenue < self.x):
                self.turnLeft()
                self.move()
            else:
                self.randMove()                   
        elif(self.rightIsClear()):
            if(self.facingNorth() and avenue < self.x):
                self.turnRight()
                self.move()
            elif(self.facingSouth() and avenue > self.x):
                self.turnRight()
                self.move()
            else:
                self.randMove()
        else:
            self.randMove()

##-----------------------------------------------------------------
#yellow ghost
class StreetFollower(Ghost):
    def __init__(self, w, x=1, y=1, d=north, b=0):
        Ghost.__init__(self,w, x, y, d, b, "pacBot", "ghost3")
        self.delay = 2 

    def makeNextMove(self, avenue, street):
        if (self.y < street):
            self.faceNorth()
            if(self.frontIsClear()):
                self.move() 
            else:
                self.randMove()
        elif (self.y > street):
            self.faceSouth()
            if(self.frontIsClear()):
                self.move()
            else:
                self.randMove()
        else:
            self.randMove()