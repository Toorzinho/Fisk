import pygame
from vector import Vector
from fish import Fish

# Start game
pygame.init()

# Create screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create 5 fish objects
fish_list = [Fish(screen) for _ in range(5)]

# Game loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for fish in fish_list:
        fish.update()
        fish.draw()

    pygame.display.flip()

pygame.quit()
