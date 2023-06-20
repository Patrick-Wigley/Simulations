import pygame,math,random
import sys, os
import pygame.math as pymath

pygame.init()
size = 1280, 600
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
pygame.display.set_caption("Water - Click anywhere above the line")

falling_objects = []
active_objects = []
timer = 0
click_boolean = True

obj_img = pygame.image.load("assets/FallingObject.png")

target_height = 450
height = target_height
tension = 0.005
dampanding = 0.005
speed = 0
spread = 0.25

point_x = 100



points = []
vertices = []
spacing = 0
vertices_length = 20
delta = 0

for i in range(vertices_length):
    spacing += 10
    point_package = [pymath.Vector2(point_x + spacing, 450), target_height, speed, delta, target_height]
    points.append(point_package)



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))


    timer += 1
    if event.type == pygame.MOUSEBUTTONDOWN and click_boolean:
        x,y = pygame.mouse.get_pos()
        falling_objects.append([obj_img, x, y])
        click_boolean = False



    elif event.type == pygame.MOUSEBUTTONUP:
        click_boolean = True



    index = -1
    active_objects = []
    vertices = []

    for check in falling_objects:
        if check[2] < 600:
            active_objects.append(check)
        else:
            falling_objects.remove(check)

       

    for line in points: 
        
        index += 1

        line[4] = (target_height - line[0].y)
        line[2] += (tension * line[4]) - (dampanding * line[2])
        line[0].y += line[2]


        if index < 19:
            right_delta = spread * (points[index][0].y - points[index + 1][0].y)
            #line[2] += right_delta
            points[index + 1][0].y += right_delta


        if index > 0:
            left_delta = spread * (points[index][0].y - points[index - 1][0].y)
           # line[2] += left_delta
            points[index - 1][0].y += left_delta




        vertices.append(line[0])
        for active in active_objects:  
            y_distance = (active[2]+5) - line[0].y 
            x_distance = (active[1] +5) - line[0].x
            
            active[2] += 0.15
            screen.blit(active[0], (active[1], active[2]))
            
           
            
            if y_distance >-5 and y_distance <5 and x_distance > -vertices_length - 1 and x_distance < vertices_length - 1:
                line[0].y -= 6
                   
                
              
    
             


    

    
    
    test = pygame.draw.aalines(screen, (255,255,255), False, vertices)
    test.contains(121,1231,123,123)


    # for collide in active_objects:
    #     check_overlap_x = collide[1] - x2
    #     check_overlap_y = collide[2] - y2  
    #     if check_overlap_x <= 5 and check_overlap_x >= -5 and check_overlap_y <= 5 and check_overlap_y >= -5:
    #         height += 10




    fps.tick(120)
    pygame.display.update()