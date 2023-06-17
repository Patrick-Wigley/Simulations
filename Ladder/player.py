import pygame


class Player():
    def __init__(self, x,y):

        self.x = x
        self.y = y

      

    def move(self, x_direction, y_direction, sprint):
        
        speed = 5
        if sprint == True:
            speed = 9

        if x_direction == "left":
            self.x -= speed
    
        elif x_direction == "right":
            self.x += speed

        if y_direction == "up":
            self.y -= speed

        elif y_direction == "down":
            self.y += speed


        



    def draw(self, screen):

        pygame.draw.circle(screen, (0,0,0), (self.x, self.y), 5, 10)

