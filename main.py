import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
import sys
from score import Score
import time

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

    score = Score()

    start_time = time.time()
    game_duration = 0

    
    powerup_1 = False
    powerup_2 = False
    powerup_3 = False

        
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_duration = time.time() - start_time
        if int(game_duration) != int(game_duration - dt):
            print(f"Game time: {int(game_duration)} seconds")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot is not None:
                shots_group.append(new_shot)    

        asteroid_field.set_game_state(game_duration, score.value)
        updatable.update(dt)
        for asteroid in asteroids:
            asteroid.set_game_state(game_duration, score.value)

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
                continue
                

        for shot in shots_group[:]:
            for asteroid in asteroids:
                if shot.is_colliding(asteroid):
                    asteroid.health -= 1
                    shots_group.remove(shot)
                    if asteroid.radius >= ASTEROID_MAX_RADIUS and asteroid.health <= 0:
                        asteroid.split()
                        score.increase(1)
                    elif asteroid.radius < ASTEROID_MAX_RADIUS and asteroid.radius > ASTEROID_MIN_RADIUS and asteroid.health <= 0:
                        asteroid.split()
                        score.increase(2)
                    elif asteroid.radius == ASTEROID_MIN_RADIUS and asteroid.health <= 0:
                        asteroid.split()
                        score.increase(3)
                    break

        if game_duration >= 10 and score.value >= 50 and not powerup_1:
            global PLAYER_SHOOT_COOLDOWN
            PLAYER_SHOOT_COOLDOWN = 0.2
            player.set_cooldown(0.2)
            player.set_color("green")
            powerup_1 = True
            print("Level 2!")

        if game_duration >= 10 and score.value >= 100 and not powerup_2:
            PLAYER_SHOOT_COOLDOWN = 0.1
            player.set_cooldown(0.1)
            player.set_color("blue")
            powerup_2 = True
            print("Level 3!")

        if game_duration >= 20 and score.value >= 150 and not powerup_3:
            PLAYER_SHOOT_COOLDOWN = 0.05
            player.set_cooldown(0.05)
            player.set_color("red")
            powerup_3 = True
            print("Level 4!")

        

        
        

        
        
        score.render(screen)
        pygame.display.flip()
        dt = clock.tick(165) / 1000

    

if __name__ == "__main__":
    main()