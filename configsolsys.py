"""
Customizable functions that determine what to display in the main animation
"""
#################################################################################
## IMPORTS

import csv
from physclasses import CelestialBody

#################################################################################
## FUNCTIONS

def _readcsv(obj):
    orbital_data = "data/orbital_elements.csv"
    with open(orbital_data) as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] == obj:
                return [float(data) for data in row[1:6]] + [row[-1]]
    
    return -1
    
    
def add_neptune(app):
    neptune_orbs = _readcsv("neptune")
    neptune = CelestialBody(name="Neptune", orbital_elements=neptune_orbs,\
        color="#3E9ED4", T=neptune_orbs[-1])
    
    app.system.add_body(neptune)

def add_uranus(app):
    uranus_orbs = _readcsv("uranus")
    uranus = CelestialBody(name="Uranus", orbital_elements=uranus_orbs,\
        color="#9DD1D4", T=uranus_orbs[-1])
    
    app.system.add_body(uranus)
    
def add_saturn(app):
    saturn_orbs = _readcsv("saturn")
    saturn = CelestialBody(name="Saturn", orbital_elements=saturn_orbs,\
        color="#D4D09D", T=saturn_orbs[-1])
    
    app.system.add_body(saturn)
    
def add_jupiter(app):
    jupiter_orbs = _readcsv("jupiter")
    jupiter = CelestialBody(name="Jupiter", orbital_elements=jupiter_orbs[0:5],\
        color="#D4B33E", T=jupiter_orbs[-1])
    
    app.system.add_body(jupiter)
    
def add_mars(app):
    mars_orbs = _readcsv("mars")
    mars = CelestialBody(name="Mars", orbital_elements=mars_orbs,\
        color="#D4563E", T=mars_orbs[-1])
    
    app.system.add_body(mars)
    
def add_earth(app):
    earth_orbs = _readcsv("earth")
    earth = CelestialBody(name="Earth", mass=5.9722e24, orbital_elements=earth_orbs,\
        color="#4B7ABB", T=earth_orbs[-1])
    
    app.system.add_body(earth)
    
def add_venus(app):
    venus_orbs = _readcsv("venus")
    venus = CelestialBody(name="Venus", mass=4.8673e24, orbital_elements=venus_orbs,\
        color="#6FBD6B", T=venus_orbs[-1])
    
    app.system.add_body(venus)
    
def add_mercury(app):
    mercury_orbs = _readcsv("mercury")
    mercury = CelestialBody(name="Mercury", mass=3.285e23, orbital_elements=mercury_orbs,\
        color="#E2721E", T=mercury_orbs[-1])
    
    app.system.add_body(mercury)
    
def solsys(app):
    
    add_jupiter(app)
    add_saturn(app)
    add_uranus(app)
    add_neptune(app)

    inner_planets(app)
    
def inner_planets(app):

    add_mercury(app)
    add_venus(app)
    add_earth(app)
    add_mars(app)

def test_object(app):
    
    add_earth(app)
    
def add_halleys(app):
    halley_orbs = _readcsv("halley")
    halley = CelestialBody(name="Halley\'s Comet", orbital_elements=halley_orbs,\
        color="#4EF0F4", T=halley_orbs[-1])
    
    app.system.add_body(halley)
    
def comets(app):
    add_earth(app)
    add_halleys(app)
    
def custom(app):
    """customizable function that can be called from main"""
    pass