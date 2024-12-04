# Probability Calculator Project

This project implements a probability calculator to estimate the probability of drawing a specific set of balls from a hat in random experiments. The program uses Monte Carlo simulations to approximate probabilities through repeated random draws.

## Project Description

Suppose there is a hat containing balls of various colors, and we want to calculate the probability of drawing a certain number of balls of specific colors in a random draw. Instead of calculating this probability using advanced mathematics, this project simulates random experiments to estimate the probability.

### Example Problem:
Given a hat containing 5 blue balls, 4 red balls, and 2 green balls, what is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? The program performs this experiment a large number of times to estimate the probability.

## Classes

### `Hat`
The `Hat` class represents a hat containing balls of different colors. The class allows you to create a hat with a variable number of balls of each color and perform random draws of a specified number of balls.

#### Methods:
- `__init__(self, **kwargs)` - Initializes the hat with the specified number of balls for each color. The colors and their counts are passed as keyword arguments. For example: `Hat(red=5, blue=3)` will create a hat with 5 red balls and 3 blue balls.
- `draw(self, num_balls)` - Draws a specified number of balls randomly from the hat. If the number of balls to draw exceeds the number of balls in the hat, all available balls will be drawn.

### `experiment`
The `experiment` function runs multiple experiments to estimate the probability of drawing a specific combination of balls from the hat.

#### Parameters:
- `hat` (Hat object) - The hat object containing the balls.
- `expected_balls` (dict) - A dictionary indicating the exact number of each color ball that you want to draw. For example, `{'red': 1, 'green': 2}` indicates you want to draw 1 red ball and 2 green balls.
- `num_balls_drawn` (int) - The number of balls to draw from the hat in each experiment.
- `num_experiments` (int) - The number of experiments to run. The more experiments, the more accurate the probability estimate.

#### Returns:
The function returns the estimated probability of drawing the expected number of balls of each color.

## How It Works
```python
1. Create a Hat:
   You create a `Hat` object by specifying the number of balls of each color. For example:
   ```python
   hat = Hat(blue=5, red=4, green=2)
This creates a hat containing 5 blue balls, 4 red balls, and 2 green balls.

2. Perform an Experiment:
The experiment function is used to simulate drawing balls from the hat.
For example, to estimate the probability of drawing at least 1 red ball and 2 green balls from the hat when drawing 4 balls:

probability = experiment(
    hat=hat,
    expected_balls={'red': 1, 'green': 2},
    num_balls_drawn=4,
    num_experiments=1000
)
print(f"Estimated probability: {probability}")
3. Monte Carlo Simulation:
The program performs a large number of random experiments (as specified by num_experiments) and counts how many times the drawn balls meet the expected conditions.
The probability is estimated as the ratio of successful experiments to the total number of experiments.

```


