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
        self.max_speed = max([o.vel for _, o in self.object_dict.items()])
        print(self.max_speed)
        self.prec_coef = self.min_prec / self.max_speed

    def update(self):
        # move every object

        new_max_speed = -float('inf')
        for name, obj in self.object_dict.items():
            pos_X, pos_Y = obj.pos
            vel_X, vel_Y = obj.vel
            acc_X, acc_Y = obj.acc

            # update position
            obj.pos = (pos_X + self.prec_coef * vel_X, pos_Y + self.prec_coef * vel_Y)

            # update acceleration
            obj.vel = (vel_X + self.prec_coef * acc_X, vel_Y + self.prec_coef * acc_Y)

            new_max_speed = max(new_max_speed, obj.vel)

        self.max_speed = new_max_speed
        self.prec_coef = self.min_prec / self.max_speed

