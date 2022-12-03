#################################################################################
## IMPORTS

import time
from datetime import date as d
from configsolsys import *
from constants import bar
from main import clear

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
        _time_sel(app)
        _date_sel(app)
        return True
    
    return False


def _time_sel(app):
    
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
    
    
def _date_sel(app):
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
        
        
def save_anim(app, anim):
    while True:
        choice = input("save animation? [y/n]: ")
        if choice.lower().strip() == "y":
            app.save(anim, "inner_planets.gif")
        elif choice.lower().strip() == "n":
            break
    
        print("invalid input")
        time.sleep(1)
        clear()