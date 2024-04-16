import pygame
import sys

class Slider:
    def __init__(self, x, y, w, h, min_val, max_val, init_val, text):
        self.rect = pygame.Rect(x, y, w, h)  # Sliderens position og størrelse
        self.min_val = min_val
        self.max_val = max_val
        self.value = init_val
        self.grabbed = False  # Holder styr på, om slideren er grebet af musen

        
        self.font = pygame.font.Font('freesansbold.ttf', 12)
 
        # create a text surface object,
        # on which text is drawn on it.
   
        self.text = self.font.render(text, True,(0,0,0))
 
        # create a rectangular object for the
        # text surface object
        self.textRect = self.text.get_rect()
 
        # set the center of the rectangular object.
        self.textRect.bottomleft = (x, y-8)

        

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.grabbed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.grabbed = False
        elif event.type == pygame.MOUSEMOTION and self.grabbed:
            self.value = ((event.pos[0] - self.rect.x) / self.rect.width) * (self.max_val - self.min_val) + self.min_val
            self.value = max(min(self.value, self.max_val), self.min_val)

    def draw(self, screen):
        # Tegn slider bar
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        # Tegn håndtag baseret på nuværende værdi
        handle_x = (self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width + self.rect.x
        pygame.draw.circle(screen, (0, 0, 0), (int(handle_x), self.rect.y + self.rect.height // 2), self.rect.height // 2)
        screen.blit(self.text, self.textRect)

    def get_value(self):
        return self.value
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    slider = Slider(50, 100, 300, 20, 0, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            slider.handle_event(event)

        screen.fill((255, 255, 255))
        slider.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
