#################################################################################
## IMPORTS

from physclasses import CelestialBody

#################################################################################
## FUNCTIONS

def solsys(app):
    neptune_orbs = [30.0699, 0.00859, 1.7700, 273.2, 131.784]
    neptune = CelestialBody(name="Neptune", orbital_elements=neptune_orbs,\
        color="lightblue")

    uranus_orbs = [19.189, 0.04726, 0.773, 96.9, 74.02]
    uranus = CelestialBody(name="Uranus", orbital_elements=uranus_orbs,\
        color="gray")

    saturn_orbs = [9.537, 0.0539, 2.486, 338.9, 113.7]
    saturn = CelestialBody(name="Saturn", orbital_elements=saturn_orbs,\
        color="beige")

    jupiter_orbs = [5.2029, 0.0484, 1.304, 274.3, 100.4]
    jupiter = CelestialBody(name="Jupiter", orbital_elements=jupiter_orbs,\
        color="beige")    

    

    app.system.add_body(neptune)
    app.system.add_body(uranus)
    app.system.add_body(saturn)
    app.system.add_body(jupiter)

    inner_planets(app)
    
def inner_planets(app):
    mars_orbs = [1.52371, 0.09339, 1.850, 286.5, 49.6]
    mars = CelestialBody(name="Mars", orbital_elements=mars_orbs,\
        color="red")

    earth_orbs = [1, 0.0167, 0, 114.208, -11.2606]
    earth = CelestialBody(name="Earth", mass=5.9722e24, orbital_elements=earth_orbs,\
        color="blue")

    venus_orbs = [0.723, 0.0068, 3.3947, 54.9, 76.7]
    venus = CelestialBody(name="Venus", mass=4.8673e24, orbital_elements=venus_orbs,\
        color="green")

    mercury_orbs = [0.3870993, 0.20564, 7.005, 29.13, 48.3]
    mercury = CelestialBody(name="Mercury", mass=3.285e23, orbital_elements=mercury_orbs,\
        color="orange")
    
    app.system.add_body(mars)
    app.system.add_body(earth)
    app.system.add_body(venus)
    app.system.add_body(mercury)

    app.ax.scatter(0,0,0,color="yellow",edgecolor="black")
    