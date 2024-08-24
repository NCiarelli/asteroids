# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # pygame initilization
    (numpass, numfail) = pygame.init()
    # print(f"{numpass} pygame modules initialized successfully")
    # print(f"{numfail} pygame modules failed to initialize")
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(SCREEN_COLOR)
        for obj in updateable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        # print(f"dt equals {dt} seconds")


if __name__ == "__main__":
    main()