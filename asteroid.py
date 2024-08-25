import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, color= ASTEROID_COLOR, center= self.position, radius= self.radius, width= ASTEROID_DRAW_LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        vel_a = self.velocity.rotate(split_angle)
        vel_b = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_a = Asteroid(self.position.x, self.position.y, new_radius)
        ast_b = Asteroid(self.position.x, self.position.y, new_radius)
        ast_a.velocity = vel_a * 1.2
        ast_b.velocity = vel_b * 1.2
