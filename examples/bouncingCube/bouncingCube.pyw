import os
import sys
import turtle as t
from random import choice, uniform, randint

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(parent_dir)

from main import draw_cube3D

def moving_cube():
    global cube_x, cube_y, cube_x_vel, cube_y_vel
    draw_cube3D(cube_x, cube_y, 0, 100, 100, 1)
    cube_x += cube_x_vel
    cube_y += cube_y_vel
    if cube_x >= 250 or cube_x <= -250:
        t.color(choice(["light blue", "light green", "light pink", "light yellow", "light coral", 
                        "light salmon", "light cyan", "powder blue", "peach puff", "lavender", 
                        "thistle", "wheat"]))
        cube_x_vel = -cube_x_vel + uniform(-1.2, 1.2)
        cube_x = max(min(cube_x, 250), -250)
    if cube_y >= 250 or cube_y <= -250:
        t.color(choice(["light blue", "light green", "light pink", "light yellow", "light coral", 
                        "light salmon", "light cyan", "powder blue", "peach puff", "lavender", 
                        "thistle", "wheat"]))
        cube_y_vel = -cube_y_vel + uniform(-1.2, 1.2)
        cube_y = max(min(cube_y, 250), -250)

if __name__ == "__main__":
    screen = t.getscreen()
    screen.title("Bouncing 3D Cube | By BravestCheetah")
    screen.setup(width=425, height=425)
    screen.bgcolor("black")
    root = screen._root
    t.speed(0)
    t.tracer(0)
    t.hideturtle()
    t.color("white")
    cube_y = randint(-200, 200)
    cube_x = randint(-200, 200)
    cube_y_vel = choice([-5, 5])
    cube_x_vel = choice([-5, 5])
    def update():
        t.clear()
        moving_cube()
        t.update()
        root.after(16, update)
    update()
    root.mainloop()
