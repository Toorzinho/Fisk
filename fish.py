import pygame
import random
from vector import Vector

WIDTH, HEIGHT = 800, 600

class Fish:
    def __init__(self, position, velocity, screen):
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.fishy = pygame.image.load('fish_image.png')
        self.fishy = pygame.transform.scale(self.fishy, (40,40))

    def update(self):
        # Bounce off the walls
        if self.position.x < 0 or self.position.x > WIDTH:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > HEIGHT:
            self.velocity.y *= -1

        self.position = self.position + self.velocity

    def draw(self):
        self.screen.blit(self.fishy,(self.position.x,self.position.y))

def generate_random_fish(screen):
    fish_list = []
    for _ in range(10):  # Adjust the number of fish as needed
        position = Vector(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        fish = Fish(position, velocity, screen)
        fish_list.append(fish)
    return fish_list
