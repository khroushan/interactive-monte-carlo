import numpy as np

class Circle:
    """ class that initialize a circle. Each circle is uniquely specified 
    by its `position` and `radius`.
    """

    def __init__(self, x0, y0, radius):
        self.x0 = x0
        self.y0 = y0
        self.radius = radius
        self.touch_boundary = False

        
    def get_position(self):
        """Return the position of the circle"""
        return (self.x0, self.y0)


    def get_radius(self):
        """ Return the radius of the circle"""
        return self.radius

    
    def move(self, x, y):
        """ Move the position of circle to the new (x,y)"""
        self.x0 = x
        self.y0 = y

        
    def expand(self, r):
        """ Increase the radius of the circle from r0 to r"""
        self.radius = r


    def __check_boundary(self, x_bound, y_bound):
        """ Check if the circle circumference touches the boundary"""
        right_x = self.x0 + self.radius
        left_x = self.x0 - self.radius
        x_condition = (right_x > x_bound) or (left_x < 0) 

        top_y = self.y0 + self.radius
        down_y = self.y0 - self.radius
        y_condition = (top_y > y_bound) or (down_y < 0)

        if (x_condition or y_condition):
            self.touch_boundary = True


class Environment(Circle):
    """ Class that control a system of circles in an environment"""

    # TODO: initialize environment by an empty env
    def __init__(self, circles, boundary):
        self.x_bound = boundary[0]
        self.y_bound = boundary[1]
        self.body = circles

    
    def get_status(self):
        """ Return the current status of the system"""
        
        status = [list(c.get_position()+(c.get_radius(),)) for c in self.body]
        # c.get_position()[0]for c in self.body
        return np.array(status)

    def run(self, time_steps=1000):
        """ Run the system with given interaction between circles"""
        for it in range(time_steps):
            # TODO: define a process to run process()
            # history[it] = self.get_status()
        pass
            
    def get_history(self):
        pass
