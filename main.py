from math import sin, cos
import pygame as pg
from cube import Cube


class PyGeo3D:
    clock = pg.time.Clock()
    projection_matrix = [
        [1, 0, 0],
        [0, 1, 0],
    ]
    cube_points = [
        [[1], [-1], [1]],
        [[1], [-1], [-1]],
        [[1], [1], [-1]],
        [[1], [1], [1]],
        [[-1], [-1], [1]],
        [[-1], [-1], [-1]],
        [[-1], [1], [-1]],
        [[-1], [1], [1]]
    ]
    RUN = True

    def __init__(self, model, res=(800, 600), fps=60):
        self.model = model
        self.res = res
        self.fps = fps
        self.window = None

    def __get_model(self):
        match self.model:
            case "cube":
                return Cube(self)

    def multiply_m(self, a, b):
        a_rows = len(a)
        a_cols = len(a[0])
        b_rows = len(b)
        b_cols = len(b[0])

        dot_product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

        if a_cols == b_rows:
            for i in range(a_rows):
                for j in range(b_cols):
                    for k in range(a_cols):
                        dot_product[i][j] += a[i][k] * b[k][j]

        return dot_product

    def connect_points(self, i, j, points):
        pg.draw.line(self.window, "white",
                     (points[i][0], points[i][1]), (points[j][0], points[j][1]))

    def make_rotation_matrix(self, angle, _type):
        if _type == 1:
            rotation_x = [
                [1, 0, 0],
                [0, cos(angle), -sin(angle)],
                [0, sin(angle), cos(angle)],
            ]
            return rotation_x

        elif _type == 2:
            rotation_y = [
                [cos(angle), 0, sin(angle)],
                [0, 1, 0],
                [-sin(angle), 0, cos(angle)],
            ]

            return rotation_y

        elif _type == 3:
            rotation_z = [
                [cos(angle), -sin(angle), 0],
                [sin(angle), cos(angle), 0],
                [0, 0, 1],
            ]
            return rotation_z

    def start(self, angles=(0.2, 0.2, 0), scale=100):
        pg.init()
        self.window = pg.display.set_mode(self.res)

        window = self.window
        model = self.__get_model()
        while self.RUN:

            window.fill("black")

            model.draw(angles, scale)

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.RUN = False

            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    a = PyGeo3D(model="cube")
    a.start(angles=(0.005, 0.01, 0))
