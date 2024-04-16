import pygame

WIDTH, HEIGHT = 800, 600

class Fish:
    def __init__(self, position, velocity, screen):
        self.position = position
        self.velocity = velocity
        self.screen = screen
        self.fishy = pygame.image.load('fish_image.png')
        self.fishy = pygame.transform.scale(self.fishy, (40,40))

           # Bounce off the walls
        if self.position.x < 0 or self.position.x > WIDTH:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > HEIGHT:
            self.velocity.y *= -1
        
    def update(self):
        self.position = self.position + self.velocity

    def draw(self):
        self.screen.blit(self.fishy,(self.position.x,self.position.y))
        

     