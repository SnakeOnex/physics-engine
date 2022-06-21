# Import and initialize the pygame library
import pygame
import numpy as np
from objects import *
from engine import Engine

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_p,
    KEYDOWN,
    KEYUP,
    QUIT,
)

def draw_world_state(screen, object_dict, mp_ratio, world_size):
    for name, obj in object_dict.items():
        obj.draw(screen, mp_ratio, world_size)

if __name__ == '__main__':
    camera_size = (500, 500)

    # in meters 
    world_size = (40, 40)

    mp_ratio = camera_size[0] / world_size[0]
    
    # min precision (in meters)
    min_prec = 0.10

    ## world init (in meters)
    object_dict = {
        "circle_1": Circle(
            radius=1.,
            pos=np.array((10.,35.)), vel=np.array((0.,0.)), 
            acc=np.array((-0.0,-0.9)),
            color=(220,0,120)
        ),
        "circle_2": Circle(
            radius=1.,
            pos=np.array((10.,25.)), 
            vel=np.array((0.,0.)), 
            acc=np.array((-0.1,-0.1)),
            color=(220,90,120)
        )
    }

    engine = Engine(object_dict, min_prec)

    # pygame init
    pygame.init()
    screen = pygame.display.set_mode(camera_size)

    clock = pygame.time.Clock()

    # Run until the user asks to quit
    running = True
    paused = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_RIGHT:
                    engine.update()

                if event.key == K_p:
                    paused = not paused
                    

        # print("frame: ", frame)
        screen.fill((255, 255, 255))

        if not paused:
            engine.update()

        # draw world
        draw_world_state(screen, engine.object_dict, mp_ratio, world_size)

        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()
        clock.tick(300)
        frame += 1

    pygame.quit()
