import pygame
import math as pymath


def find_distance(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    hypot = pymath.sqrt((p1x - p2x)**2 + (p1y - p2y)**2)
    return hypot


def find_last_index(indexs):
    largest_number = 0
    for number, index in enumerate(indexs):
        if number > largest_number:
            largest_number = number
    return largest_number


def create_points(quantity):
    objects = []
    for _ in range(2):
        distancing = 1.0
        for _ in range(quantity):
            objects.append(Points(1.0, 1.0, distancing))
            distancing += 1.1
    return objects


def create_connections(quantity, spacing):
    lines = []
    for i in range(quantity - 1):
        lines.append([i, i + 1, spacing - 10])

    # VERTICES ON OTHER SIDE OF ROPE
    for i in range(quantity - 1):
        lines.append([i, i + quantity, spacing - 10])

    for i in range(quantity - 1):
        lines.append([i + quantity, i + 1 + quantity, spacing - 10])

    return lines



class Points():
    def __init__(self, x,y, spacing):
        self.x = x
        self.y = y + spacing
        
        self.old_x = x
        self.old_y = y + spacing

        self.origanal_x = x
        self.origanal_y = y + spacing

        self.draw_point = []
        
        self.colour = (255,0,0)
        self.pinned = False




class Rope():
    def __init__(self, quantity, spacing, scale):
        self.quantity_perline = quantity + 1
        self.quantity = quantity - 1    # AS INDEXS (STARTING AT ZERO)
        self.scale = scale
        self.spacing = spacing
        self.points = create_points(quantity + 1)
        self.lines = create_connections(quantity + 1, spacing)
        self.last_index = find_last_index(self.points)       
        self.overall_len = 0
        self.grab_timer = 0




    def interia(self, player):
        for _, point in enumerate(self.points):
            velocity_x = point.x - point.old_x
            velocity_y = point.y - point.old_y

            point.old_x = point.x
            point.old_y = point.y

            point.x += velocity_x
            point.y += velocity_y
            point.y += 0.05



    def verlet(self):
        for line in self.lines:
            hypotenuse = find_distance(( self.points[line[0]].x, self.points[line[0]].y), (self.points[line[1]].x, self.points[line[1]].y))
            offset = (line[2]) - hypotenuse
            fix = offset / hypotenuse /  2

            distance_x = self.points[line[1]].x - self.points[line[0]].x
            distance_y = self.points[line[1]].y - self.points[line[0]].y

            self.points[line[0]].x -= distance_x * fix 
            self.points[line[0]].y -= distance_y * fix 
            
            self.points[line[1]].x += distance_x * fix
            self.points[line[1]].y += distance_y * fix 



    def set_position(self, position, mouse, player, grabbed):
        self.grab_timer += 1

        self.overall_len = find_distance((self.points[0].x, self.points[0].y), (self.points[13].x, self.points[13].y))
        if self.overall_len > 38:
            grabbed = True          

        for index, point in enumerate(self.points):
            if index != 0 and index != self.quantity_perline: 
                point.draw_point = []

            if index == 0:
                point.x = point.origanal_x + position[0] / self.scale
                point.y = point.origanal_y + position[1] / self.scale
                self.points[self.quantity_perline].x = (point.origanal_x + 5) + position[0] / self.scale
                self.points[self.quantity_perline].y = (point.origanal_y) + position[1] / self.scale

                point.draw_point = [point.x * self.scale, point.y * self.scale]
                self.points[self.quantity_perline].draw_point = [self.points[7].x * self.scale, self.points[7].y * self.scale]

            elif index == 6 or index == 13:
                if  mouse[0] > (point.x * self.scale) - 30 and mouse[0] < (point.x * self.scale) + 30  and  mouse[1] > (point.y * self.scale) - 30 and mouse[1] < (point.y * self.scale) + 30 and grabbed:
                    self.points[6].pinned = True
                    self.points[13].pinned = True

                if point.pinned == True and grabbed == True and self.grab_timer > 3:
                    self.points[6].x = (mouse[0]) / self.scale
                    self.points[6].y = mouse[1] / self.scale
                    self.points[13].x = (mouse[0]) / self.scale
                    self.points[13].y = mouse[1] / self.scale         
                
                elif point.pinned:
                    self.points[6].pinned = False
                    self.points[13].pinned = False

                    self.grab_timer = 0
                    
            if index != 0 and index != self.quantity_perline:
                point.draw_point = [point.x * self.scale, point.y * self.scale]



    def draw(self, screen, player):
        for lines in self.lines:            
            if player.y > self.points[lines[0]].y * self.scale and player.y < self.points[lines[1]].y * self.scale :
            
                self.points[lines[0]].colour = [0,0,0]
                self.points[lines[1]].colour = [0,0,0]
            
            else:
                self.points[lines[0]].colour = [135, 86, 56]
                self.points[lines[1]].colour = [135, 86, 56]

            pygame.draw.line(screen, self.points[lines[0]].colour, (self.points[lines[0]].draw_point), (self.points[lines[1]].draw_point), 7)
            pygame.draw.circle(screen, (0,0,0), (self.points[lines[0]].draw_point), 6, 12)
            