import pygame
from constants import *
from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shot_time = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), PLAYER_DRAW_LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    
    def update(self, dt):
        self.shot_time -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward_vector = pygame.Vector2(0, 1)
        forward_vector = forward_vector.rotate(self.rotation)
        forward_vector = forward_vector * PLAYER_SPEED * dt
        self.position += forward_vector
    
    def shoot(self):
        if self.shot_time > 0:
            return
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_time = PLAYER_SHOOT_COOLDOWN