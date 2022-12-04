#################################################################################
## IMPORTS

import time
from datetime import date as d
from datetime import datetime as dt
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
        "minor":minor_planets,"select":select_adds, "custom":custom, "exit":_exit}
    
    while True:
        print("Select Action")
        print(bar)
        print(f"{'show the inner solar system: ':{'.'}<30}{' inner':{'.'}>23}")
        print(f"{'show the full solar system: ':{'.'}<30}{' full':{'.'}>23}")
        print(f"{'show earth and comets: ':{'.'}<30}{' comets':{'.'}>23}")
        print(f"{'show earth and minor planets: ':{'.'}<30}{' minor':{'.'}>23}")
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
    """user input for determining the animation time, fps, and interval"""
    tim = []
    
    while True:
        print(bar)
        print("input the total time (days), speed of the animation")
        print("(fps) and the interval between animated frames (days)")
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
                    print(f"{selection} is not an integer")
                    OK = False
                
            if OK:
                clear()
                break
        
        print("incorrect format")
        time.sleep(1)
        clear()           
    
    
def _date_sel(app):
    """user input for determining the date"""
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
    """user input for saving the animation"""
    while True:
        choice = input("save animation? [y/n]: ")
        if choice.lower().strip() == "y":
            name = str(dt.now()).replace(' ', '-')
            name = name[:name.find(".")].replace(':', '-')
            app.save(anim, f"animations/astroanim{name}.gif")
            break
        elif choice.lower().strip() == "n":
            break
    
        print("invalid input")
        time.sleep(1)
        clear()
        
        
def select_adds(app):
    """user input for selecting what bodeis to show"""
    opts = {"mer": add_mercury, "ven": add_venus, "ear": add_earth,\
        "mar": add_mars, "jup": add_jupiter, "sat": add_saturn,\
        "ura": add_uranus, "nep": add_neptune, "hal": add_halleys,\
        "plu": add_pluto, "cer": add_ceres, "eri": add_eris,\
        "mak": add_makemake, "hau": add_haumea, "sol": solsys,\
        "inn": inner_planets, "cus": custom}
    
    running = True
    
    while running:
    
        print("Select Orbital Bodies")
        print(bar)
        print("select what to animate, format: ")
        print("input: opt1 opt2 opt3 ...")
        print(bar)
        print(f"{'Mercury: ':{'.'}<21}{' mer':<4} | {'Venus: ':{'.'}<21}{' ven':<4}")
        print(f"{'Earth: ':{'.'}<21}{' ear':<4} | {'Mars: ':{'.'}<21}{' mar':<4}")
        print(f"{'Jupiter: ':{'.'}<21}{' jup':<4} | {'Saturn: ':{'.'}<21}{' sat':<4}")
        print(f"{'Uranus: ':{'.'}<21}{' ura':<4} | {'Neptune: ':{'.'}<21}{' nep':<4}")
        print(f"{'Halleys: ':{'.'}<21}{' hal':<4} | {'Pluto: ':{'.'}<21}{' plu':<4}")
        print(f"{'Ceres: ':{'.'}<21}{' cer':<4} | {'Eris: ':{'.'}<21}{' eri':<4}")
        print(f"{'Makemake: ':{'.'}<21}{' mak':<4} | {'Haumea: ':{'.'}<21}{' hau':<4}")
        print(f"{'Solar system: ':{'.'}<21}{' sol':<4} | {'Inner planets: ':{'.'}<21}{' inn':<4}")
        print(f"{'Custom: ':{'.'}<21}{' cus':<4} |")
        print(bar)
        options = input("input: ").split(" ")
        
        for opt in options:
            if opt in opts.keys():
                running = False
                opts[opt](app)
            else:
                print(f"{opt} is not an option")
                
        clear()
