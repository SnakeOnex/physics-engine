# Import and initialize the pygame library
import pygame
from objects import *
from engine import Engine

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

def draw_world_state(screen, object_dict):
    for name, obj in object_dict.items():
        obj.draw(screen)

if __name__ == '__main__':
    camera_size = (500, 500)

    ## world init
    object_dict = {
        "circle_1": Circle(radius=10,pos=(100,100), vel=(5,5), color=(220,0,120)),
        "circle_2": Circle(radius=10,pos=(150,150), vel=(0,0), color=(220,90,120))
    }

    engine = Engine(object_dict)

    # pygame init
    pygame.init()
    screen = pygame.display.set_mode(camera_size)

    clock = pygame.time.Clock()

    # Run until the user asks to quit
    running = True
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
                    print("engine update")

        print("frame: ", frame)
        screen.fill((255, 255, 255))

        # draw world
        draw_world_state(screen, engine.object_dict)

        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()
        clock.tick(30)
        frame += 1

    pygame.quit()
