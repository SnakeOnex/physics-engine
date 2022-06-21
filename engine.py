import numpy as np
import sys

class Engine():
    def __init__(self, object_dict, min_prec):
        """
        args:
          object_dict {
            world_size: (int, int)
          }
          min_prec - max step size
        """
        self.object_dict = object_dict
        self.min_prec = min_prec

        # find max speed
        ## todo: max ABSOLUTE speed
        self.max_speed = max([np.abs(o.vel).max() for _, o in self.object_dict.items()])
        print(self.max_speed)
        self.prec_coef = self.min_prec / self.max_speed if self.max_speed != 0 else 1.

    def update(self):

        # 1. check for colissions 

        # 2. move every object
        new_max_speed = -float('inf')
        self.print_objects()
        print("max speed: ", self.max_speed)
        print("prec coef: ", self.prec_coef)

        for name, obj in self.object_dict.items():
            pos_X, pos_Y = obj.pos
            vel_X, vel_Y = obj.vel
            acc_X, acc_Y = obj.acc

            # update position
            obj.pos = obj.pos + self.prec_coef * obj.vel

            # update acceleration
            obj.vel = obj.vel + self.prec_coef * obj.acc

            new_max_speed = max(new_max_speed, np.abs(obj.vel).max())

        self.max_speed = new_max_speed
        self.prec_coef = self.min_prec / self.max_speed if self.max_speed != 0 else 1.


    def print_objects(self):
        for name, obj in self.object_dict.items():
            print(f"{name}: {obj.pos}")
