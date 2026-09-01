# Name: 
# Only fill in the methods (# write code here) to complete each task

from pyKarel import *

def main():       
    wld=World("tasks99", delay=0.1)
    
    t1 = Robot(wld, 1, 1, east, 0, "fish") 
    t2 = Robot(wld, 1, 2, east, 0, "gorilla") 
    t3 = Robot(wld, 1, 3, east, 0, "mouse")
    t4 = Robot(wld, 1, 4, east, 0, "shark")
    t5 = Robot(wld, 1, 5, east, 0, "wolf") 
    t6 = Robot(wld, 1, 6, east, 0, "worstFear") 
    t7 = Robot(wld, 1, 7, east, 0, "link") 

    followBeeperRoad(t1)	  #go to the end of the row of beepers
    findTheBeeper(t2)        #go to the beeper
    findTheWall(t3)	        #go to the wall
    findTheWallAndClean(t4)	  #go to the wall, pick up all the beepers (max one per pile)
    followBeeperRoadAndReturn(t5)	#Go to end of the row of beepers and return back to the starting point.  
    findTheBeeperAndReturn(t6)    #go to the beeper and return to starting position.
    findTheWallAndReturn(t7) #go to the wall and return to starting position.
    
    wld.mainloop()


def followBeeperRoad(temp):	  #go to the end of the row of beepers
    pass    
    # delete pass (for temporary compile) and write code here    


def findTheBeeper(temp):    #go to the beeper
    pass    
    # delete pass (for temporary compile) and write code here


def findTheWall(temp):	  #go to the wall
    pass    
    # delete pass (for temporary compile) and write code here


def findTheWallAndClean(temp):	  #go to the wall, pick up all the beepers (max one per pile)
    pass    
    # delete pass (for temporary compile) and write code here
     

def followBeeperRoadAndReturn(temp):	#Go to end of the row of beepers and return back to the starting point.  
    pass    
    # delete pass (for temporary compile) and write code here     


def findTheBeeperAndReturn(temp):    #go to the beeper and return to starting position.
    pass    
    # delete pass (for temporary compile) and write code here   


def findTheWallAndReturn(temp): #go to the wall and return to starting position.
    pass    
    # delete pass (for temporary compile) and write code here


if __name__=="__main__":
     main()
 