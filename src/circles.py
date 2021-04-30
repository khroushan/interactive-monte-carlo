import numpy as np
import numpy.random as rnd

class Circle:
    """ class that initialize a circle. Each circle is uniquely specified 
    by its `position` and `radius`.
    """

    def __init__(self, x0, y0, radius):
        self.x0 = x0
        self.y0 = y0
        self.radius = radius
        self.touch_boundary = False

    def __repr__(self):
        return f"c at {(self.x0, self.y0)} with r = {self.radius}"
        
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
        
    def expand(self, delta_r):
        """ Increase the radius of the circle from r0 to r"""
        self.radius += delta_r

    def _is_in(self, x,y):
        """Check if the `point` falls into the circle"""
        xc, yc = self.x0, self.y0
        cond = ((x-xc)**2 + (y-yc)**2) <= self.get_radius()
        return cond
    
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


class Environment():
    """ Class that control a system of circles in an environment"""

    # TODO: initialize environment by an empty env
    # TODO: check of circles are instatiated as object circle
    def __init__(self, circles, boundary):
        self.x_bound = boundary[0]
        self.y_bound = boundary[1]
        self.body = circles

    def _rn_generator(self, n_steps):
        x_rand = rnd.uniform(size=n_steps, high=self.x_bound)
        y_rand = rnd.uniform(size=n_steps, high=self.y_bound)
        return x_rand, y_rand
    
    def get_state(self):
        """ Return the current status of the system"""
        state = [list(c.get_position()+(c.get_radius(),)) for c in self.body]
        # c.get_position()[0]for c in self.body
        return np.array(state)

    def _which_circle(self,x,y):
        return [c for c in self.body if c._is_in(x,y)]

    def run(self, n_steps: int, eps:float = 0.1):
        """ Run a system for given timesteps"""
        x_rand, y_rand = self._rn_generator(n_steps)
        delta_r = eps
        for x,y in zip(x_rand,y_rand):
            circles = self._which_circle(x,y)
            for c in circles:
                c.expand(delta_r)
    
    # def run(self, time_steps=1000):
    #     """ Run the system with given interaction between circles"""
    #     for it in range(time_steps):
    #         # TODO: define a process to run process()
    #         # history[it] = self.get_state()
    #         pass
    #     pass
            
    def get_history(self):
        pass
