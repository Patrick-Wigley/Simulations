import pygame
import sys
from ClothObjects import Rope
from player import Player


# NOTE: Maybe the player could grab the last two points of the rope 
# (dangle strings) & place it into the ground quickly where he is standing.
# If the rope is not planted into the ground the player cannot climb therefore,
# if on the rope, he will fall off.

pygame.init()
TEXT_LINES = [
        "NOTE:",
        "WASD to move dot/player",
        "Click around bottom of ladder to provoke some inertia",
        ]


size = width,height = 700, 350
screen = pygame.display.set_mode(size)
Frame_Rate = pygame.time.Clock()
pygame.display.set_caption("Monster-Manic - Ladder Example")

key_font = pygame.font.SysFont("Verdana", 15)

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

        cloth.interia()
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


    for i, line in enumerate(TEXT_LINES):
        text = key_font.render(
                        line,
                        True,
                        (255,0,0)
                        )
        screen.blit(text, (0, i*15))


    Frame_Rate.tick(80)
    pygame.display.update()