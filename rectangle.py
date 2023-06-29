from main import PyGeo3D

class Cube(PyGeo3D):
    def __init__(self):
        super().__init__(self)
    
    def draw_cube(self, angles, scale):
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
