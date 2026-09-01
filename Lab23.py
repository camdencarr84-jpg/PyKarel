# Do not modify this code, just use to test run

from Seeker import *
from random import randint

def main():
    wld=World()
    beeperLocation = randint(1,5)
    height_of_wall = beeperLocation + randint(1,5)
    wld.addWall(1, 1, 1, height_of_wall)
    wld.addBeeper(2, beeperLocation)
      
    karel = Seeker(wld, d=north, b=0)
    karel.fetchBeeper()
    karel.putBeeper()
    wld.mainloop()

if __name__=="__main__":
   main()
