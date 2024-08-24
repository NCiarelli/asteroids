# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # pygame initilization
    (numpass, numfail) = pygame.init()
    # print(f"{numpass} pygame modules initialized successfully")
    # print(f"{numfail} pygame modules failed to initialize")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    asteroid_field = AsteroidField()


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Shot.containers = (shots, updateable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(SCREEN_COLOR)
        for obj in updateable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for ast in asteroids:
            if player.is_colliding(ast):
                print("Game over!")
                sys.exit()
        for ast in asteroids:
            for shot in shots:
                if ast.is_colliding(shot):
                    ast.kill()
                    shot.kill()
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        # print(f"dt equals {dt} seconds")


if __name__ == "__main__":
    main()