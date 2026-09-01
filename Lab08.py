# Do not modify this code, just use to test run

from pyKarel import *
from Racers import *
import sys

def race(arg):
    while not arg.onABeeper():
        if arg.frontIsClear():
          arg.move()  
        else:
          arg.jumpRight()  
          
def main():
    name_of_world = input("Which 'hurdle', 'steeple', or 'boxtop' world? ")
    kind_of_racer = input("What kind of racer? ")

    wld=World(name_of_world, width=20, height=10, delay=0.1)
   
    if  kind_of_racer == "Racer":
        jesse_owens = Racer(wld,1)
    elif kind_of_racer == "SteepleRacer":
        jesse_owens = SteepleRacer(wld,1)
    elif kind_of_racer == "BoxRacer":
        jesse_owens = BoxRacer(wld,1)
    elif kind_of_racer == "Athlete":
        jesse_owens = Athlete(wld)
    elif kind_of_racer == "Robot":
        jesse_owens = Robot(wld)
    else:
        print("Invalid robot type.")
        sys.exit(0)
    race(jesse_owens)    
    wld.mainloop()

if __name__=="__main__":
   main()

##  End of file
