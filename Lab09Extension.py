# Name:
# Do not modify this code, just use to test run

from pyKarel import *
from Shifter import *

def main():
    name_of_world=raw_input("Which 'pile' world? ")
    wld=World(name_of_world, width=8, height=3, delay=0.1)
    r = Shifter(wld, 1,1, east)
    r.shift_piles()
    wld.mainloop()
    
if __name__=="__main__":
    main()          
       
    

