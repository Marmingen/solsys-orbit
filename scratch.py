import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from physclasses import CelestialBody


def update(frame, planets, times):
    for planet in planets:
        #planet.calc_pos(times[frame])
        planet._offsets3d = (times[frame],0,0)
    return planets

fig = plt.figure()
ax = p3.Axes3D(fig)

earth_orbs = [1, 0.0167, 0, 114.208, -11.2606]
earth = CelestialBody(name="Earth", mass=5.9722e24, orbital_elements=earth_orbs,\
    color="blue")

venus_orbs = [0.723, 0.0068, 3.3947, 54.9, 76.7]
venus = CelestialBody(name="Venus", mass=4.8673e24, orbital_elements=venus_orbs,\
    color="green")

planets = [ax.scatter(earth.pos.x, earth.pos.y, earth.pos.z),\
    ax.scatter(venus.pos.x, venus.pos.y, venus.pos.z)]

ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

times = range(200)

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update, 25, fargs=(planets, times),
                              interval=50, blit=False)

plt.show()