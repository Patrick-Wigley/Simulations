import pygame
import sys
from ClothObjects import Rope
from player import Player


# NOTE: Maybe the player could grab the last two points of the rope 
# (dangle strings) & place it into the ground quickly where he is standing.
# If the rope is not planted into the ground the player cannot climb therefore,
# if on the rope, he will fall off.


size = width,height = 700, 350
screen = pygame.display.set_mode(size)
Frame_Rate = pygame.time.Clock()
pygame.display.set_caption("Monster-Manic - Ladder Example")


player = Player(100, height/2)
x_direction = "none"
y_direction = "none"


cloth = Rope(6, 25, 7)
cloth2 = Rope(6, 15, 7)
ropes = [cloth2]


mouse_grabbed = False

while True:
    screen.fill((0,0,255))
    key = pygame.key.get_pressed()
    mx,my = pygame.mouse.get_pos()

    mouse_grabbed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
        if event.type == pygame.KEYDOWN:
            if key[pygame.K_1]:
                cloth2.grab_timer = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_grabbed = True
        

    offset = width /2 + 50
    for cloth in ropes:

        cloth.interia(player)
        cloth.verlet()
        cloth.set_position((offset, 0), (mx,my), player, mouse_grabbed)
        cloth.draw(screen, player)
        

    x_direction = "none"
    y_direction = "none"
    sprint = False
    if key[pygame.K_d]:
        x_direction = "right"
    elif key[pygame.K_a]:
        x_direction = "left"
    
    if key[pygame.K_w]:
        y_direction = "up"
    elif key[pygame.K_s]:
        y_direction = "down"

    if key[pygame.K_LSHIFT]:
        sprint = True


    player.move(x_direction, y_direction, sprint)
    player.draw(screen)


    Frame_Rate.tick(80)
    pygame.display.update()