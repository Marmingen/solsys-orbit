# Solar System Orbital Animation

This little program displays select orbital bodies and creates an animation over a select period of time. It does not simulate the motion of the orbits, merely calculates it out of the orbital elements. Any other object the user would like to be added can be done by editing the csv file under data, as well as creating an addition function for it in `configsolsys.py`.

## Typical result

The user will specify the bodies and the period of the animation. Below is a typical result of animating a year passed by the inner planets.

![oneyear](https://user-images.githubusercontent.com/106428188/205493487-c7c5a586-6e39-49aa-a124-fcdee576bf52.gif)

## See historical passages

The user can specify the exact date and time for the start of the animation.

![halley_pass](https://user-images.githubusercontent.com/106428188/205494007-08c95107-c99e-4db4-aeb1-b650e38550a4.gif)

As seen above you can use this program to see historical passages, such as the 1986 perihelion of Halley's comet.

## How to install

- Clone the repository
- Run `install.py`
- Run `main.py`

## Guide to input

In the main-selection, the input `exit` will safely exit the program.

### Predefined packages

The inputs `inner`, `full`, `comets`, and `minors` will run predefined packages of solar system objects. More information about these packages and what they entail can be deducted from the `configsolsys.py` file. The package `custom` is preallocated as a package to be changed and determined by the user.  

### User selection of bodies

By the `select` input, the user can choose exactly what bodies to animate. The bodies will all have their own key-tag, as well as the predefined packages. The format is defined as key-tags separated by a space:
`input: key1 key2 key3...`
Overloaded key-tags will be ignored.

### Animation period input

This is when the user will specify the animation period and parameters. The input is in the format of `time` `speed` `interval`:
- `time`: total time to animate [days]
- `speed`: final speed of the animation [frames per second]
- `interval`: the interval between frames [days]

### Date input

This is when the user will specify the start date of the animation. Format: YYYY-MM-DD-HH. Input `today` to automatically select today's date.
Be aware that dates before 1524 will be slightly incorrect, leading up to very incorrect for dates < year 400. 
