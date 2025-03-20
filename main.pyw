import turtle as t
from random import randint, choice, uniform
import winsound

cam_y = 0
cam_x = 0
cam_z = 15
fov = 10

def goto3D(x: float, y: float, z: float) -> None:
    if (z + cam_z) != 0:
        screen_x = ((x - cam_x) * fov) / (z + cam_z)
        screen_y = ((y - cam_y) * fov) / (z + cam_z)
        t.goto(screen_x, screen_y)

def draw_line3D(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> None:
    t.up()
    goto3D(x1, y1, z1)
    t.down()
    goto3D(x2, y2, z2)
    t.up()

def draw_cube3D(x: float, y: float, z: float, scale_x: float, scale_y: float, scale_z: float) -> None:
    half_x = scale_x * 0.5
    half_y = scale_y * 0.5
    half_z = scale_z * 0.5
    vertices = [
        (x - half_x, y - half_y, z - half_z),
        (x + half_x, y - half_y, z - half_z),
        (x + half_x, y + half_y, z - half_z),
        (x - half_x, y + half_y, z - half_z),
        (x - half_x, y - half_y, z + half_z),
        (x + half_x, y - half_y, z + half_z),
        (x + half_x, y + half_y, z + half_z),
        (x - half_x, y + half_y, z + half_z),
    ]
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    for edge in edges:
        v1, v2 = edge
        draw_line3D(
            vertices[v1][0], vertices[v1][1], vertices[v1][2],
            vertices[v2][0], vertices[v2][1], vertices[v2][2]
        )

def moving_cube():
    global cube_x, cube_y, cube_x_vel, cube_y_vel
    draw_cube3D(cube_x, cube_y, 0, 100, 100, 1)
    cube_x += cube_x_vel
    cube_y += cube_y_vel
    if cube_x >= 250 or cube_x <= -250:
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        t.color(choice(["light blue", "light green", "light pink", "light yellow", "light coral", "light salmon", "light cyan", "powder blue", "peach puff", "lavender", "thistle", "wheat"]))
        cube_x_vel = -cube_x_vel + uniform(-1.2, 1.2)
        cube_x = max(min(cube_x, 250), -250)
    if cube_y >= 250 or cube_y <= -250:
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        t.color(choice(["light blue", "light green", "light pink", "light yellow", "light coral", "light salmon", "light cyan", "powder blue", "peach puff", "lavender", "thistle", "wheat"]))
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
    #preload sound to prevent glitches
    winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    winsound.PlaySound(None, winsound.SND_ASYNC)
    def update():
        t.clear()
        moving_cube()
        t.update()
        root.after(16, update)
    update()
    root.mainloop()
