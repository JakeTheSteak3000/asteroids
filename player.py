import pygame
from circleshape import *
from constants import *
from pygame.math import Vector2
from shot import Shot
from constants import PLAYER_SHOOT_SPEED
import math



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.color = "white"

    
    # Add the triangle method from the instructions
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Add the draw method we just discussed
    def set_color(self, new_color):
        self.color = new_color
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)

        # Clamp the player's position within the screen boundaries
        self.position.x = max(self.radius, min(self.position.x, SCREEN_WIDTH - self.radius))
        self.position.y = max(self.radius, min(self.position.y, SCREEN_HEIGHT - self.radius))
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return None
        
        self.timer = PLAYER_SHOOT_COOLDOWN
        ship_points = self.triangle()
        front_point = ship_points[0]
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        new_shot = Shot(front_point, shot_velocity, self.color)

        
        return new_shot
    
    def set_cooldown(self, new_cooldown):
        self.timer = 0
        global PLAYER_SHOOT_COOLDOWN
        PLAYER_SHOOT_COOLDOWN = new_cooldown
    




