import copy
import random

class Hat:
    """
    A class to represent a hat containing balls of different colors.

    The hat is initialized with a given number of balls of different colors. 
    The draw method allows you to randomly draw a specified number of balls from the hat.
    If the number of balls to draw exceeds the number available, it will return all the balls.
    """

    def __init__(self, **kwargs):
        """
        Initializes the hat with balls of various colors. 
        Colors and their quantities are passed as key-value pairs.
        For example: Hat(red=3, blue=2) will create a hat with 3 red balls and 2 blue balls.
        """
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """
        Draws a specified number of balls at random from the hat.
        If num_balls is greater than the total number of balls in the hat, it returns all available balls.
        """
        if num_balls >= len(self.contents):  # If trying to draw more balls than available
            all_balls = self.contents[:]  # Copy all balls
            self.contents = []  # Empty the hat
            return all_balls
        
        # If there are enough balls, draw a random number without replacement
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove the selected balls from the contents
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Runs a specified number of experiments to estimate the probability 
    of drawing certain balls from a hat.

    hat: A Hat object containing the balls.
    expected_balls: A dictionary specifying the expected number of balls to be drawn for each color.
    num_balls_drawn: The number of balls to be drawn in each experiment.
    num_experiments: The total number of experiments to perform.

    Returns the estimated probability of drawing the expected balls.
    """
    successful_experiments = 0  # Counter for successful experiments

    for _ in range(num_experiments):
        # Create a copy of the hat
        hat_copy = copy.deepcopy(hat)
        
        # Draw balls randomly
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the balls drawn
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1
        
        # Check if the drawn balls meet the expected condition
        success = True
        for ball, count in expected_balls.items():
            if drawn_count.get(ball, 0) < count:
                success = False
                break
        
        if success:
            successful_experiments += 1

    # Calculate the probability
    probability = successful_experiments / num_experiments
    return probability


