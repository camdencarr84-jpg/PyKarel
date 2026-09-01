# This is demonstrating the example shown in the
# discussion titled 'Stored Recursive Calls'

from pyKarel import *

## Recursive solution
def recursive(arg):
    if arg.onABeeper():    # base case
        arg.pickBeeper()
        arg.turnLeft()
    else:
        arg.move()
        recursive(arg)             # recursive call
        arg.move()             # this command is stored; eventually it is executed

## Iterative solution 
def iterative(arg):
    count = 0
    while not arg.onABeeper():
        arg.move()
        count = count + 1
    arg.pickBeeper()
    arg.turnLeft()
    for k in range (count):
       arg.move()
    


def main():     
    user = input("Which solution (R)ecursive or (I)terative? ")
    wld = World("Lab21Discussion")
    karel = Robot(wld,1,1,east,0)
    if(user == "R" or user == "r"):
        recursive(karel)
    else:
        iterative(karel)
    karel.putBeeper()
    wld.mainloop()

if __name__=="__main__":
   main()
