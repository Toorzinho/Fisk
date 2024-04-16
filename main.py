import pygame
from vector import Vector
from fish import Fish, generate_random_fish

# Start game
pygame.init()

# Create screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fish_list = generate_random_fish(screen)

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
