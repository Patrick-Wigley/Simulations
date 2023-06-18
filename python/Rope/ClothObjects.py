import pygame
import math as pymath


def create_objects(quantity):
    spacing = 1.0
    my_objects = []
    for i in range(quantity):
        my_objects.append(ClothObjects(1.0, 1.0, spacing))
        spacing += 1.1                                          # SOLVED: SPACING CANNOT BE A WHOLE NUMBER - (MUST BE FLOAT)

    return my_objects


def create_index_connections(quantity):
    '''Sets list for the connections of each vertex. '''
                                                                        #                  All this list is is the connections which will be looked at in the calculations below. It is basically ( current index & index + 1).
    connections = []                                                                     
    for i in range(quantity - 1):                                    
        connections.append([i, i+1, 5])

    return connections




def calculate_hypot(p1X, p1Y, p2X, p2Y):
    ''' find distance between point1 (X & Y) and point2 (X & Y) '''

    hypotenuse = pymath.sqrt((p1X - p2X)** 2 + (p1Y - p2Y)** 2)

    return hypotenuse

    


class ClothObjects():
    def __init__(self, x,y, spacing):
        self.x = x
        self.y = y + spacing

        self.old_x = x
        self.old_y = y + spacing

        self.origanal_x = x
        self.origanal_y = y + spacing





class Main():
    """Params: Quantity of points;  Scale/Size of points;   Spacing intended; """
    def __init__(self, quantity, scale, spacing):
        

        self.scale = scale
        self.spacing = spacing

        self.points = create_objects(quantity)

        self.connections = create_index_connections(quantity)



    def motion(self):
        '''Interia'''   

        for point in self.points:

            velocity_x = point.x - point.old_x
            velocity_y = point.y - point.old_y

            point.old_x = point.x
            point.old_y = point.y

            point.x += velocity_x
            point.y += velocity_y
            point.y += 0.05
                                                                      # interia Algorithm


    
    def verlet(self):
        ''' Verlet'''

        
        for point in self.connections:

            distance = calculate_hypot(self.points[point[0]].x, self.points[point[0]].y, self.points[point[1]].x, self.points[point[1]].y)
            distance_difference = point[2] - distance
            fix = distance_difference / distance / 2

            difference_x = self.points[point[1]].x - self.points[point[0]].x
            difference_y = self.points[point[1]].y - self.points[point[0]].y

            self.points[point[0]].x -= difference_x * fix
            self.points[point[0]].y -= difference_y * fix

            self.points[point[1]].x += difference_x * fix
            self.points[point[1]].y += difference_y * fix
                                                                        # Verlet Algorithm
                                                                       
  
  
  
    def set_placement(self, width):
        ''' Places main (top vertex) '''

        for i, point in enumerate(self.points):
            if i == 0:
                point.x = point.origanal_x + (width/2) / self.scale
                point.y = point.origanal_y + 0 / self.scale
                point.old_x = point.x
                point.old_y = point.y




    def alter(self, mouse):
        ''' Param:  [MouseX, MouseY];
        Alters points if collision'''
        
        mx = mouse[0]
        my = mouse[1]

        for point in self.points:
            if mx < (point.x * self.scale) + 30 and mx > (point.x * self.scale) - 30 and  my < (point.y * self.scale) + 30 and my > (point.y * self.scale) - 30:
                point.x = mx / self.scale
                point.y = my / self.scale
                                                       



    def draw(self, screen):
        ''' Param:  Screen which is being displayed;
        Scales & draws vertices & lines connecting'''


        points_scaled = []

        for size in self.points:
            point_x = size.x * self.scale
            point_y = size.y * self.scale
            points_scaled.append([point_x, point_y])

  
        for draw in self.connections:
            pygame.draw.line(screen, (135, 86, 56), (points_scaled[draw[0]][0], points_scaled[draw[0]][1]), (points_scaled[draw[1]][0], points_scaled[draw[1]][1]), 15)
            

            pygame.draw.circle(screen, (0,0,0), (points_scaled[draw[0]][0], points_scaled[draw[0]][1]), 10, 20)




            



        