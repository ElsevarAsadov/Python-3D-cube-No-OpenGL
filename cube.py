import pygame as pg


class Cube:
    def __init__(self, pygeo):
        self.pygeo = pygeo
        self.angle_x = self.angle_y = self.angle_z = 0

    def draw(self, angles, scale):
        pygeo = self.pygeo
        window = pygeo.window
        self.angle_x += angles[0]
        self.angle_y += angles[1]
        self.angle_z += angles[2]

        points = []

        for point in pygeo.cube_points:
            r = pygeo.make_rotation_matrix(self.angle_x, 1)
            rotation = pygeo.multiply_m(r, point)

            if angles[1]:
                r = pygeo.make_rotation_matrix(self.angle_y, 2)
                rotation = pygeo.multiply_m(r, rotation)

            if angles[2]:
                r = pygeo.make_rotation_matrix(self.angle_z, 3)
                rotation = pygeo.multiply_m(r, rotation)

            point_2d = pygeo.multiply_m(pygeo.projection_matrix, rotation)

            x = (point_2d[0][0] * scale) + pygeo.res[0] / 2
            y = (point_2d[1][0] * scale) + pygeo.res[1] / 2

            points.append((x, y))
            pg.draw.circle(window, "red", (int(x), int(y)), 5)

        for i in range(4):
            pygeo.connect_points(i, (i + 1) % 4, points)
            pygeo.connect_points(i, (i + 4), points)
            pygeo.connect_points(i+4, ((i+1) % 4) + 4, points)
