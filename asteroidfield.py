import pygame
import random
from asteroid import *
from constants import *
from score import Score


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.game_duration = 0
        self.score_value = 0
        self.diff_2 = False
        self.diff_3 = False
        self.diff_4 = False
        self.new_rate = ASTEROID_SPAWN_RATE

    def set_game_state(self, duration, score):
        self.game_duration = duration
        self.score_value = score

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        if self.game_duration >= 30 and self.score_value >= 250:
            asteroid.health = 2
            if not self.diff_2:
                print("Difficulty 2!")
                self.diff_2 = True
        if self.game_duration >= 40 and self.score_value >= 400:
            asteroid.health = 3
            if not self.diff_3:
                print("Difficulty 3!")
                self.diff_3 = True
        if self.game_duration >= 50 and self.score_value >= 600:
            asteroid.health = 4
            if not self.diff_4:
                print("Difficulty 4!")
                self.diff_4 = True
        

    def update(self, dt):
        if self.score_value >= 2000 and not hasattr(self, 'spawn_rate_mod3'):
            self.new_rate = self.new_rate * 0.1
            self.spawn_rate_mod3 = True
            self.spawn_timer += dt
            if self.spawn_timer > self.new_rate:
                self.spawn_timer = 0

                # spawn a new asteroid at a random edge
                edge = random.choice(self.edges)
                speed = random.randint(40, 100)
                velocity = edge[0] * speed
                velocity = velocity.rotate(random.randint(-30, 30))
                position = edge[1](random.uniform(0, 1))
                kind = random.randint(1, ASTEROID_KINDS)
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
        elif self.score_value >= 1500 and not hasattr(self, 'spawn_rate_mod2'):
            self.new_rate = self.new_rate * 0.25
            self.spawn_rate_mod2 = True
            self.spawn_timer += dt
            if self.spawn_timer > self.new_rate:
                self.spawn_timer = 0

                # spawn a new asteroid at a random edge
                edge = random.choice(self.edges)
                speed = random.randint(40, 100)
                velocity = edge[0] * speed
                velocity = velocity.rotate(random.randint(-30, 30))
                position = edge[1](random.uniform(0, 1))
                kind = random.randint(1, ASTEROID_KINDS)
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
        elif self.score_value >= 1000 and not hasattr(self, 'spawn_rate_mod'):
            self.new_rate = self.new_rate * 0.5
            self.spawn_rate_mod = True
            self.spawn_timer += dt
            if self.spawn_timer > self.new_rate:
                self.spawn_timer = 0

                # spawn a new asteroid at a random edge
                edge = random.choice(self.edges)
                speed = random.randint(40, 100)
                velocity = edge[0] * speed
                velocity = velocity.rotate(random.randint(-30, 30))
                position = edge[1](random.uniform(0, 1))
                kind = random.randint(1, ASTEROID_KINDS)
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
        else:
            self.spawn_timer += dt
            if self.spawn_timer > self.new_rate:
                self.spawn_timer = 0

                # spawn a new asteroid at a random edge
                edge = random.choice(self.edges)
                speed = random.randint(40, 100)
                velocity = edge[0] * speed
                velocity = velocity.rotate(random.randint(-30, 30))
                position = edge[1](random.uniform(0, 1))
                kind = random.randint(1, ASTEROID_KINDS)
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

    def set_game_state(self, duration, score):
        self.score_value = score
        self.game_duration = duration
