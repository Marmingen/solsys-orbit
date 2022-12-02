#################################################################################
## IMPORTS

from App import App
from physclasses import *
from configsolsys import *

#################################################################################
## MAIN

def main():

    app = App()

    #star = CelestialBody(color="yellow")
    
    #inner_planets(app)
    
    solsys(app)
    
    #app.system.add_body(earth)
    
    #app.system.add_body(star)

    app.draw_body()

    app.draw_ellipse()

    app.show()

    #anim = app.animate()
    
    #app.show()
    
    for i in range(100):
        #app.animate()
        app.update()
        app.show()
        app.close()


if __name__ == "__main__":
    main()