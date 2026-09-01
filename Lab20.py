# Do not modify this code, just use to test run

from Politicians import *
import sys

def escape(arg):
    while not arg.onABeeper():
        arg.turnToTheNextSegment()
        arg.walkDownCurrentSegment()

def main():
    world = input("Which 'maze'? ")
    wld= World(world, width=8, height=8, delay=0.1)
    kind = input("What kind of politician? (D, R, or I) ")
    if  kind == "D" or kind == "d":
        candidate = Democrat(wld)
    elif kind == "R" or kind == "r":
        candidate = Republican(wld)
    elif kind == "I" or kind == "i":
        candidate = Independant(wld)
    else:
        print ("Wrong kind")
        sys.exit(0)                 # exists gracefully, if needed
    escape( candidate )
    wld.mainloop()

if __name__=="__main__":
    main()