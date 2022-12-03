#################################################################################
## IMPORTS

from App import App
from physclasses import *
from configsolsys import *

#################################################################################
## MAIN

def main():

    app = App(200,1,10, date="2022-12-03-00")

    inner_planets(app)
    
    #solsys(app)
    
    #test_object(app)
    
    app.initial_calculation()

    anim = app.animate()
    
    app.show()
    
    
#################################################################################
## RUN CODE

if __name__ == "__main__":
    main()