"""
Customizable functions that determine what to display in the main animation
"""
#################################################################################
## IMPORTS

import csv
from physclasses import CelestialBody

#################################################################################
## CSV READER

def _readcsv(obj):
    """reads the data in orbital_elements.csv, edit this csv with recent data"""
    orbital_data = "data/orbital_elements.csv"
    with open(orbital_data) as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] == obj:
                return [float(data) for data in row[1:6]] + [row[-1]]
    
    return -1
    
#################################################################################
## ADDITION FUNCTION

#####################################
## addition of planet

# adds neptune
def add_neptune(app):
    neptune_orbs = _readcsv("neptune")
    neptune = CelestialBody(name="Neptune", orbital_elements=neptune_orbs,\
        color="#3E9ED4", T=neptune_orbs[-1])
    
    app.system.add_body(neptune)

# adds uranus
def add_uranus(app):
    uranus_orbs = _readcsv("uranus")
    uranus = CelestialBody(name="Uranus", orbital_elements=uranus_orbs,\
        color="#9DD1D4", T=uranus_orbs[-1])
    
    app.system.add_body(uranus)
    
# adds saturn
def add_saturn(app):
    saturn_orbs = _readcsv("saturn")
    saturn = CelestialBody(name="Saturn", orbital_elements=saturn_orbs,\
        color="#D4D09D", T=saturn_orbs[-1])
    
    app.system.add_body(saturn)
    
# adds jupiter
def add_jupiter(app):
    jupiter_orbs = _readcsv("jupiter")
    jupiter = CelestialBody(name="Jupiter", orbital_elements=jupiter_orbs[0:5],\
        color="#D4B33E", T=jupiter_orbs[-1])
    
    app.system.add_body(jupiter)
    
# adds mars
def add_mars(app):
    mars_orbs = _readcsv("mars")
    mars = CelestialBody(name="Mars", orbital_elements=mars_orbs,\
        color="#D4563E", T=mars_orbs[-1])
    
    app.system.add_body(mars)
    
# adds earth
def add_earth(app):
    earth_orbs = _readcsv("earth")
    earth = CelestialBody(name="Earth", mass=5.9722e24, orbital_elements=earth_orbs,\
        color="#4B7ABB", T=earth_orbs[-1])
    
    app.system.add_body(earth)
    
# adds venus
def add_venus(app):
    venus_orbs = _readcsv("venus")
    venus = CelestialBody(name="Venus", mass=4.8673e24, orbital_elements=venus_orbs,\
        color="#6FBD6B", T=venus_orbs[-1])
    
    app.system.add_body(venus)
    
# adds mercury
def add_mercury(app):
    mercury_orbs = _readcsv("mercury")
    mercury = CelestialBody(name="Mercury", mass=3.285e23, orbital_elements=mercury_orbs,\
        color="#E2721E", T=mercury_orbs[-1])
    
    app.system.add_body(mercury)
    
#####################################
## addition of comets
    
def add_halleys(app):
    halley_orbs = _readcsv("halley")
    halley = CelestialBody(name="Halley\'s Comet", orbital_elements=halley_orbs,\
        color="#4EF0F4", T=halley_orbs[-1])
    
    app.system.add_body(halley)
    
def add_halebopp(app):
    hbop_orbs = _readcsv("halebopp")
    hbop = CelestialBody(name="Hale-Bopp", orbital_elements=hbop_orbs,\
        color="#4EF0F4", T=hbop_orbs[-1])
    
    app.system.add_body(hbop)

def add_hyaku(app):
    hyaku_orbs = _readcsv("hyakutake")
    hyaku = CelestialBody(name="Hyakutake", orbital_elements=hyaku_orbs,\
        color="#4EF0F4", T=hyaku_orbs[-1])
    
    app.system.add_body(hyaku)

def add_tempeltuttle(app):
    tempel_orbs = _readcsv("tempeltuttle")
    tempel = CelestialBody(name="Tempel-Tuttle", orbital_elements=tempel_orbs,\
        color="#4EF0F4", T=tempel_orbs[-1])
    
    app.system.add_body(tempel)
    
def add_swifttuttle(app):
    swift_orbs = _readcsv("swifttuttle")
    swift = CelestialBody(name="Swift-Tuttle", orbital_elements=swift_orbs,\
        color="#4EF0F4", T=swift_orbs[-1])
    
    app.system.add_body(swift)

#####################################
## addition of minor bodies

def add_pluto(app):
    pluto_orbs = _readcsv("pluto")
    pluto = CelestialBody(name="Pluto", orbital_elements=pluto_orbs,\
        color="#D23286", T=pluto_orbs[-1])
    
    app.system.add_body(pluto)
    
def add_ceres(app):
    ceres_orbs = _readcsv("ceres")
    ceres = CelestialBody(name="Ceres", orbital_elements=ceres_orbs,\
        color="#AF487E", T=ceres_orbs[-1])
    
    app.system.add_body(ceres)

def add_eris(app):
    eris_orbs = _readcsv("eris")
    eris = CelestialBody(name="Eris", orbital_elements=eris_orbs,\
        color="#954F74", T=eris_orbs[-1])
    
    app.system.add_body(eris)

def add_makemake(app):
    makemake_orbs = _readcsv("makemake")
    makemake = CelestialBody(name="Makemake", orbital_elements=makemake_orbs,\
        color="#B76E94", T=makemake_orbs[-1])
    
    app.system.add_body(makemake)

def add_haumea(app):
    haumea_orbs = _readcsv("haumea")
    haumea = CelestialBody(name="Pluto", orbital_elements=haumea_orbs,\
        color="#D49DBA", T=haumea_orbs[-1])
    
    app.system.add_body(haumea)
    
#####################################
## bundles

# adds the entire solar system
def solsys(app):
    inner_planets(app)
    
    add_jupiter(app)
    add_saturn(app)
    add_uranus(app)
    add_neptune(app)

# adds the inner planets
def inner_planets(app):
    add_mercury(app)
    add_venus(app)
    add_earth(app)
    add_mars(app)

# adds comets
def comets(app):
    add_earth(app)
    add_halleys(app)
    add_halebopp(app)
    add_hyaku(app)
    add_tempeltuttle(app)
    add_swifttuttle(app)

# adds minor planets
def minor_planets(app):
    add_pluto(app)
    add_ceres(app)
    add_eris(app)
    add_makemake(app)
    add_haumea(app)
    
    add_earth(app)
    
#####################################
## custom bundle
    
def custom(app):
    """customizable function that can be called from main"""
    pass

#####################################
## object for testing

def test_object(app):
    
    add_earth(app)
    # add_halebopp(app)
    # add_hyaku(app)
    add_tempeltuttle(app)