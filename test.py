from src.circles import Circle, Environment

c0 = Circle(1,1,0.5)
c1 = Circle(2,2,1.)
c2 = Circle(2,1,0.5)
c3 = Circle(1,2,0.5)

print(f"c0 radius:{c0.get_radius()}")
print(f"c1 position:{c1.get_position()}")
# Environement is defined by boundary and a list of circles

env0 = Environment([c0, c1, c2, c3],
                   (5, 5))


