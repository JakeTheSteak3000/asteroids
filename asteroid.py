import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.health = 1
        self.color = "white"

    def set_color(self, new_color):
        self.color = new_color
    
    def draw(self, screen, new_color=None):
        # Define colors as RGB tuples
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        ORANGE = (255, 165, 0)
        
        # Determine the color based on health
        if self.health == 1:
            color_to_use = WHITE
        elif self.health == 2:
            color_to_use = YELLOW
        elif self.health == 3:
            color_to_use = ORANGE
        elif self.health == 4:
            color_to_use = RED
        else:
            color_to_use = WHITE
        
        # Use new_color if provided
        if new_color is not None:
            color_to_use = new_color
            
        # Draw the asteroid
        pygame.draw.circle(
            screen,

            (255, 0, 0),

            color_to_use,

            (self.position.x, self.position.y),
            self.radius,
            2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 * 1.2
        self.health = 1
        if self.game_duration >= 30 and self.score_value >= 250:
            asteroid1.health = 2
            asteroid2.health = 2
        if self.game_duration >= 40 and self.score_value >= 400:
            asteroid1.health = 3
            asteroid2.health = 3
        if self.game_duration >= 50 and self.score_value >= 600:
            asteroid1.health = 4
            asteroid2.health = 4

    def set_game_state(self, duration, score):
        self.game_duration = duration
        self.score_value = score

