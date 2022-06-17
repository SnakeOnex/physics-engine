
class Engine():
    def __init__(self, object_dict):
        """
        args:
          params - dict {
            world_size: (int, int)
          }
        """
        self.object_dict = object_dict

    def update(self):
        # move every object
        for name, obj in self.object_dict.items():
            pos_X, pos_Y = obj.pos
            vel_X, vel_Y = obj.vel

            obj.pos = (pos_X + vel_X, pos_Y + vel_Y)
