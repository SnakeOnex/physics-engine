import pygame

class Circle():
    def __init__(self, radius, pos, vel, color):
        self.radius = radius
        self.pos = pos
        self.vel = vel
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

