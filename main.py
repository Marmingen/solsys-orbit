#################################################################################
## IMPORTS

import time
import os
from datetime import date as d
from App import App
from physclasses import *
from configsolsys import *
from constants import bar

#################################################################################
## GLOBALS

clear = lambda: os.system('cls')

#################################################################################
## FUNCTIONS

def menu(app):

    
    selection = True  
    
    def _exit(app):
        pass
  
    choices = {"inner": inner_planets, "full":solsys, "comets": comets,\
        "select":print, "custom":custom, "exit":_exit}
    
    while True:
        print("Select Action")
        print(bar)
        print(f"{'show the inner solar system: ':{'.'}<30}{' inner':{'.'}>23}")
        print(f"{'show the full solar system: ':{'.'}<30}{' full':{'.'}>23}")
        print(f"{'show earth and comets: ':{'.'}<30}{' comets':{'.'}>23}")
        print(f"{'select what to show: ':{'.'}<30}{' select':{'.'}>23}")
        print(f"{'show the custom selection: ':{'.'}<30}{' custom':{'.'}>23}")
        print(f"{'exit the program: ':{'.'}<30}{' exit':{'.'}>23}")
        print(bar)
        
        choice = input("input: ")
        clear()
        
        if choice in choices.keys():
            if choice == "exit":
                selection = False
            choices[choice](app)
            break
        
        print("incorrect input")
        clear()
        
    if selection:
        time_sel(app)
        date_sel(app)
        return True
    
    return False


def time_sel(app):
    
    tim = []
    
    while True:
        print(bar)
        print("input the total time (days), speed of the animation (fps)")
        print("and the interval between animated frames (days)")
        print("format:")
        print("input: time speed interval")
        print(bar)
        tim = input("input: ").split(" ")
        
        if len(tim) == 3:
            
            OK = True
            
            for selection, attrib in zip(tim, [app.set_time, app.set_speed,\
                app.set_interval]):
                try:
                    attrib(int(selection))
                except:
                    print(f"{selection} is not a number")
                    OK = False
                
            if OK:
                clear()
                break
        
        print("incorrect format")
        time.sleep(1)
        clear()           
    
    
def date_sel(app):
    date = ""
    
    while True:
        print(bar)
        print("input the start date of the animation")
        print("format:")
        print("input: YYYY-MM-DD-HH")
        print("input: today for todays date")
        print(bar)
        date = input("input: ")
        
        if date == "today":
            app.set_date(str(d.today())+"-00")  
            clear()
            break      
        elif len(date.split("-")) == 4:
            app.set_date(date)
            clear()
            break
        
        print("incorrect format")
        time.sleep(1)
        clear()        
    
    
#################################################################################
## MAIN

def main():
    
    running = True
    
    while running:
        app = App()

        running = menu(app)
        
        if not running:
            break
        
        #test_object(app)
        
        app.initial_calculation()

        anim = app.animate()
        
        #app.save(anim, "inner_planets.gif")
    
    
#################################################################################
## RUN CODE

if __name__ == "__main__":
    main()
    
    print("exiting...")
    time.sleep(1)