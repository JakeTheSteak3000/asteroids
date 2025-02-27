import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    shots_group = []
        
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot is not None:
                shots_group.append(new_shot)    

        updatable.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                sys.exit()
        
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen) 

        for shot in shots_group[:]:
            shot.update(dt)
            shot.draw(screen)
            if shot.position.x < 0 or shot.position.x > SCREEN_WIDTH or \
            shot.position.y < 0 or shot.position.y > SCREEN_HEIGHT:
                shots_group.remove(shot)

        for shot in shots_group[:]:
            for asteroid in asteroids:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shots_group.remove(shot)
        
        

        
        
        pygame.display.flip()
        dt = clock.tick(165) / 1000

    

if __name__ == "__main__":
    main()