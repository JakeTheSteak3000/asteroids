import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys

def main():
    pygame.init()

    Font = pygame.font.SysFont("ninjago", 30)

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
    score = 0

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
                print(score)
                print("Game over!")
                sys.exit()

        screen.fill("black")
        # Render the score dynamically
        score_text = Font.render(f"Score: {score}", False, "white", "black")
        screen.blit(score_text, (10, 10))  # Position the score at the top-left corner

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
                    score += 1
                    asteroid.split()
                    try:
                        shots_group.remove(shot)
                    except:
                        pass

        pygame.display.flip()
        dt = clock.tick(165) / 1000


if __name__ == "__main__":
    main()
