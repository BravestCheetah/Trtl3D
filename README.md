----------------------------- **Trtl3D - The new 3D** -----------------------------
***
*The not so good 3D engine*

Trtl3D is a (bad) 3D engine entirely developed with built in python modules and math.
Its a simple renderer that uses turtle (therefore the name) to render lines and by using math it can render 3D object wireframes.
As of now objects has to be hardcoded, but to make that just a tad bit easier i have added som basic functions, like goto3D that takes in xyz coordinates and moves the turtle sprite to that location on the 2D canvas. 
There are also functions such as draw_line3D that, you guessed it, draws a line in 3D space. It takes in 2 sets of xyz coordinates and draws a line between them.
There is also draw_cube3D, well after all of the above i think its quite self explanatory, it takes in an xyz and also the width, height and lenght in form of scale_x, scale_y and scale_z.
Now sometime when im bored im gonna compile this to an actual library but for now this is how it works, go cry about it
***
**How to use**

Clone this repo or download main.py, add it to your project and directly import the functions from the file.

***
**Examples**

Currently there are 1 example(s):
- **Bouncing Cube**, like the dvd logo, but 3d, and bad.

to run these examples clone the repo or downlaod the whole thing and run the python file in the folder of the examples (example forlders are located in the folder "examples")
***
Trtl3D - A terrible 3D engine by BravestCheetah
