import vector as v
import pygame

class Fish:
    def __init__(self, position, velocity, screen):
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.fishy = pygame.image.load('fish_image.png')
        self.fishy = pygame.transform.scale(self.fishy, (40,40))
        
    def update(self):
        self.position = self.position + self.velocity

    def draw(self):
        self.screen.blit(self.fishy,(self.position.x,self.position.y))
        

     