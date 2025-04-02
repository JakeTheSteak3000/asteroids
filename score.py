import pygame
import constants
from asteroid import Asteroid

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(r"SigmaBoyDemo-DY8ym.ttf", 36)

    def increase(self, points):
        self.value += points

    def render(self, surface):
        score_text = self.font.render(f"Score: {self.value}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))

