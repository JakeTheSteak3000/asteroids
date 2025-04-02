import pygame
from circleshape import CircleShape
from constants import *
from pygame.math import Vector2

class Shot(CircleShape):
    def __init__(self, position, velocity, color="white"):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
        self.color = color

    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
