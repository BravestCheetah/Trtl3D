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