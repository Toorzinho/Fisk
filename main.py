import pygame  
import vector as v
import fish as f

#Start game
pygame.init()

#Create screen
screen =  pygame.display.set_mode((800,600))

position1 = v.Vector(400,300)
velocity1 = v.Vector(1,1)
fish1 = f.Fish(position1, velocity1,screen)

fish1.draw()
pygame.display.flip()

# Game loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    fish1.draw()

    pygame.display.flip()



