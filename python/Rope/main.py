import pygame,sys
from ClothObjects import Main

width,height = 800, 1000
screen_size = (width, height)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Vine Simulation Example - FOR MONSTER MANIC")
cloth = Main(10, 15, 10)  # ALTER ROPE: VERTICES QUANTITY, SCALING - (SIZING OF ROPE ENTIRLEY), SPACING 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    screen.fill((255,255,255))
    
    mouse = pygame.mouse.get_pos()
    
    cloth.motion()
    cloth.verlet()
    cloth.set_placement(width)    
    cloth.alter(mouse)
    cloth.draw(screen)

    clock.tick(60)
    pygame.display.update()
