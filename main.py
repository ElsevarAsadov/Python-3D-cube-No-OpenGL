from math import sin, cos
import pygame as pg


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

    def __multiply_m(self, a, b):
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
      pg.draw.line(self.window, "white", (points[i][0], points[i][1]), (points[j][0], points[j][1]))

    def __make_rotation_matrix(self, angle, _type):
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
        
        angle_x = angle_y = angle_z = 0
        window = self.window
        
        while self.RUN:
          
          window.fill("black")
              
          angle_x += angles[0]
          angle_y += angles[1]
          angle_z += angles[2]
              
          for e in pg.event.get():
              if e.type == pg.QUIT:
                  self.RUN = False
                      
          points = []
          for point in self.cube_points:
                
            r = self.__make_rotation_matrix(angle_x, 1)
            rotation = self.__multiply_m(r, point)
              
            if angles[1] :
              r = self.__make_rotation_matrix(angle_y, 2)
              rotation = self.__multiply_m(r, rotation)
              
            if angles[2] : 
              r = self.__make_rotation_matrix(angle_z, 3)
              rotation = self.__multiply_m(r, rotation)
            
            point_2d = self.__multiply_m(self.projection_matrix, rotation)

            x = (point_2d[0][0] * scale) + self.res[0] / 2
            y = (point_2d[1][0] * scale) + self.res[1] / 2

            points.append((x, y))
            pg.draw.circle(window, "red", (int(x), int(y)), 5)

          for i in range(4):
              self.connect_points(i, (i + 1) % 4, points)
              self.connect_points(i, (i + 4), points)
              self.connect_points(i+4, ((i+1) % 4) + 4, points)
                
          pg.display.update()
          self.clock.tick(self.fps)


if __name__ == "__main__":
    a = PyGeo3D(model="cube")
    a.start(angles=(0.0005, 0.01, 0))
