import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color= ASTEROID_COLOR, center= self.position, radius= self.radius, width= ASTEROID_DRAW_LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt