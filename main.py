#################################################################################
## IMPORTS

import time
import os
from App import App
from physclasses import *
from user_input import *

#################################################################################
## GLOBALS

clear = lambda: os.system('cls')
    
#################################################################################
## MAIN

def main():
    
    running = True
    
    while running:
        app = App()

        running = menu(app)
        
        if not running:
            break
        
        app.initial_calculation()

        anim = app.animate()
        
        save_anim(app, anim)
        
        print("initializing new animation")
        time.sleep(1)
        clear()
    
#################################################################################
## RUN CODE

if __name__ == "__main__":
    main()
    
    print("exiting...")
    time.sleep(1)