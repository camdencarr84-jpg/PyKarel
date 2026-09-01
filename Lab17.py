# Name: 
# Only fill in the methods (# write code here) to complete each task
# Program will crash (infinite loop) until methods are fixed

from pyKarel import *
from random import randint

global SIZE 
SIZE = 10		#controls the size of the world and the array sizes

#post: counts and returns the total number of Robots in a list a whose fronts are blocked or 
#      whose avenue >= SIZE 
def numDone(a):         #a is a list of Robots
   # **************************
   #
   return 0 #tempory, delete this --- write code here
   #
   # ***************************

#post: counts and returns the total number of Robots in a list a whose (fronts are blocked or 
#      whose avenue >= SIZE) and that are not facing SOUTH
def numWinners(a):      #a is a list of Robots
   # **************************
   #
   return 0 #tempory, delete this --- write code here
   #
   # ***************************


 #post:  advance arg's position if it is not at a wall or the enemy camp (avenue >= SIZE)
 #	    if we collide with an enemy robot, face arg south and move towards the bottom of the field
def advance(arg):
   if arg.facingWest() and arg.x==1:	#made it to the enemy base, so stop
      return
   if arg.facingEast() and arg.x==SIZE:#made it to the enemy base, so stop
      return
   if arg.y==1:								#left the playing field, so stop
      return
   if arg.onARobot():					   #here, we get kicked off the playing field
      while not arg.facingSouth():		#make arg face South and move off the field
         arg.turnLeft()
      while arg.frontIsClear():
         arg.move()
   else:										
      if arg.frontIsClear() and randint(0,1) == 0: #flip a coin to see if we move
         arg.move()
      

def main():
   wld=World(delay=0.05,width=SIZE+1, height = SIZE+1)
   squad = []
   army = []
   for i in range(SIZE):
      squad.append(Robot(wld, 1, i+2, east, 0, "knight"))
      army.append(Robot(wld, SIZE, i+2, west, 0, "worstFear"))

   squadCount = 0
   armyCount = 0
   while (squadCount + armyCount) < (SIZE*2):
      for i in range(SIZE):
         if randint(0,1) == 0: 				#to be fair, flip a coin to see who moves first
            advance(squad[i])
            advance(army[i])
         else:
            advance(army[i])
            advance(squad[i])
      squadCount = numDone(squad)
      armyCount = numDone(army)
   squadCount = numWinners(squad)
   armyCount = numWinners(army)

   if squadCount > armyCount:
      print("Knights wins by " + str(squadCount - armyCount))
   else:
      if squadCount < armyCount:
         print("Elephants wins by " + str(armyCount - squadCount))
      else:
         print("It's a TRAP!...I mean...a tie.")
   wld.mainloop()   

if __name__=="__main__": 
 main()