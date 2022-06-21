import pygame

class Circle():
    def __init__(self, radius, pos, vel, acc, color):
        self.radius = radius
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.color = color

    def draw(self, screen, mp_coef, world_size):
        # pos_px = [pos * mp_coef for pos in self.pos]
        pos_px = self.pos * mp_coef

        # invert y avis
        pos_px[1] = world_size[1] * mp_coef - pos_px[1]

        rad_px = self.radius * mp_coef
        # print("pos_px: ", pos_px)
        # print("rad_px: ", rad_px)
        pygame.draw.circle(screen, self.color, pos_px, rad_px)
