# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #creating managing goups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)


    #game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Gamer over!")
                sys.exit(0)

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        #limit the frame rate to 60 fps
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
