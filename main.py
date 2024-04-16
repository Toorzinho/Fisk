import pygame
import sys
from vector import Vector
from fish import Fish
from slider import Slider

# Start game
pygame.init()

# Create screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create slider
slider = Slider(50, 50, 300, 20, 1, 10, 5, "Number of Fish")

# Initial number of fish
num_fish = int(slider.get_value())
fish_list = [Fish(screen) for _ in range(num_fish)]

# Game loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        slider.handle_event(event)  # Handle slider events

    # Update number of fish based on slider value
    new_num_fish = int(slider.get_value())
    if new_num_fish != num_fish:
        fish_list = [Fish(screen) for _ in range(new_num_fish)]
        num_fish = new_num_fish

    for fish in fish_list:
        fish.update()
        fish.draw()

    # Draw slider
    slider.draw(screen)

    pygame.display.flip()

pygame.quit()
