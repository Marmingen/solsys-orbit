#################################################################################
## IMPORTS

from App import App
from physclasses import *
from configsolsys import *

#################################################################################
## MAIN

def main():

    app = App(200)

    inner_planets(app)
    
    #solsys(app)
    
    #test_object(app)
    
    app.initial_calculation()

    anim = app.animate()
    
    app.show()
    
    
    


if __name__ == "__main__":
    main()