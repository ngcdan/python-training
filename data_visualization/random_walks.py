from random import choice

""" Make random decisions about which direction the walk should take. """

class RandomWalk:
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walker(self):
        """Calculate all the points in the walk."""
        # Keep talking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.

            # returns either 1 for right movement or -1 for left.
            x_direction = choice([1, -1])

            # how far to move in that direction (x_direction)
            x_distance = choice([0, 1, 2, 3, 4])

            # A positive result for x_step means move right, a negative result means move left, and 0 means move vertically.
            x_step = x_direction * x_distance


            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            # A pos for y_step -> move up, a neg -> move left, and 0 -> move horizontally.
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.(both x_step and y_step are 0, the walk doesn't go anywhere, so we ignore this move)
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

